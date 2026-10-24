import streamlit as st

from sections import conclusions, deep_dives, intro, overview
from utils.io import LICENSE, SOURCE, load_data
from utils.prep import SOURCES, clean, make_tables, quality_report

st.set_page_config(page_title="Renewable electricity in France", layout="wide")


@st.cache_data(show_spinner="Loading data...")
def get_data():
    raw = load_data()
    df = clean(raw)
    return df, quality_report(raw, df)


def render_sidebar(df):
    with st.sidebar:
        st.header("Filters")
        first_year, last_year = int(df["year"].min()), int(df["year"].max())
        years = st.slider("Years", first_year, last_year, (first_year, last_year))
        all_regions = sorted(df["region"].unique())
        regions = st.multiselect("Regions", all_regions, default=all_regions)
        sources = st.multiselect(
            "Sources",
            SOURCES,
            default=SOURCES,
            help="Renewable electricity sources.",
        )
    return years, regions, sources


def filter_data(df, years, regions, sources):
    return df[
        df["year"].between(*years)
        & df["region"].isin(regions)
        & df["source"].isin(sources)
    ]


def render_footer():
    st.divider()
    st.caption("Done by: Nazim MEKIDECHE :)")


def main():
    df, quality = get_data()

    st.title("Renewable electricity in France: who produces what?")
    st.caption(f"Source: {SOURCE} | License: {LICENSE}")

    years, regions, sources = render_sidebar(df)
    filtered = filter_data(df, years, regions, sources)
    if filtered.empty:
        st.warning("No data for these filters.")
        st.stop()

    tables = make_tables(filtered)
    tabs = st.tabs(["Context", "Overview", "Deep dives", "Conclusions"])
    section_views = [
        (tabs[0], lambda: intro.show()),
        (tabs[1], lambda: overview.show(filtered, tables)),
        (tabs[2], lambda: deep_dives.show(tables)),
        (tabs[3], lambda: conclusions.show(quality)),
    ]

    for tab, view in section_views:
        with tab:
            view()
            render_footer()


main()
