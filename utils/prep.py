"""Clean the data and build the tables used by the charts."""
import pandas as pd

# French column names of the file -> short English names used in the project
COLUMN_MAP = {
    "Annee": "year",
    "Nom INSEE région": "region",
    "Production hydraulique renouvelable (GWh)": "Hydro",
    "Production bioénergies renouvelable (GWh)": "Bioenergy",
    "Production éolienne renouvelable (GWh)": "Wind",
    "Production solaire renouvelable (GWh)": "Solar",
    "Production électrique renouvelable (GWh)": "total_gwh",
    "Production gaz renouvelable (GWh)": "gas_gwh",
    "Géo-point région": "point",
}
SOURCES = ["Hydro", "Bioenergy", "Wind", "Solar"]


def _normalize_columns(raw):
    """Return a copy of the raw frame with the project's canonical column names."""
    return raw.rename(columns=COLUMN_MAP).copy()


def clean(raw):
    """Wide table (one column per source) -> long table (one row per region, year, source)."""
    df = _normalize_columns(raw).drop_duplicates()
    coords = df["point"].str.split(",", n=1, expand=True)
    df[["lat", "lon"]] = coords.apply(pd.to_numeric, errors="coerce")
    df[SOURCES] = df[SOURCES].fillna(0)  # a few empty cells: treated as 0 (see data quality)
    long = df.melt(
        id_vars=["year", "region", "lat", "lon"],
        value_vars=SOURCES,
        var_name="source",
        value_name="gwh",
    )
    long["twh"] = long["gwh"] / 1000  # 1 TWh = 1000 GWh, easier to read
    return long


def quality_report(raw, clean_df):
    """Simple data quality checks shown in the app."""
    df = _normalize_columns(raw)
    parts_sum = df[SOURCES].fillna(0).sum(axis=1)
    return {
        "Rows": len(df),
        "Regions": int(clean_df["region"].nunique()),
        "Years": f"{clean_df['year'].min()} - {clean_df['year'].max()}",
        "Duplicate rows": int(df.duplicated().sum()),
        "Missing wind values": int(df["Wind"].isna().sum()),
        "Missing bioenergy values": int(df["Bioenergy"].isna().sum()),
        "Missing renewable gas values (%)": round(df["gas_gwh"].isna().mean() * 100, 1),
        "Rows where sources do not add up to the total": int(((parts_sum - df["total_gwh"]).abs() > 1).sum()),
    }


def make_tables(df):
    """Pre-aggregated tables for the charts."""
    last_year = df["year"].max()
    return {
        "national": df.groupby(["year", "source"], as_index=False)["twh"].sum(),
        "by_region_year": df.groupby(["year", "region", "source"], as_index=False)["twh"].sum(),
        "latest": df[df["year"] == last_year].copy(),
    }
