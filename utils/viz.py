"""All charts, with the same style and labelled axes."""
import plotly.express as px
import plotly.graph_objects as go

COLORS = {"Hydro": "#1f77b4", "Bioenergy": "#2ca02c", "Wind": "#17becf", "Solar": "#ff7f0e"}
UNIT = "TWh"


def area_chart(national, title):
    fig = px.area(national, x="year", y="twh", color="source", color_discrete_map=COLORS, title=title,
                  labels={"year": "Year", "twh": f"Production ({UNIT})", "source": "Source"})
    # Annotation: total production of the last year
    last = national["year"].max()
    total = national[national["year"] == last]["twh"].sum()
    fig.add_annotation(x=last, y=total, text=f"{total:.0f} TWh in {last}", showarrow=True, ax=-70, ay=-30)
    return fig


def bar_chart(latest, n, title):
    totals = latest.groupby("region")["twh"].sum().nlargest(n).index
    data = latest[latest["region"].isin(totals)]
    fig = px.bar(data, x="twh", y="region", color="source", orientation="h", color_discrete_map=COLORS,
                 title=title, labels={"twh": f"Production ({UNIT})", "region": "Region", "source": "Source"})
    # Reference line: average production of all regions
    average = latest.groupby("region")["twh"].sum().mean()
    fig.add_vline(x=average, line_dash="dash", line_color="white")
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode="lines",
        name="Average",
        line={"color": "white", "dash": "dash"},
    ))
    return fig.update_yaxes(categoryorder="total ascending")


def map_chart(latest, title):
    regions = latest.groupby(["region", "lat", "lon"], as_index=False)["twh"].sum()
    fig = px.scatter_map(regions, lat="lat", lon="lon", size="twh", color="twh",
                         center={"lat": 46.6, "lon": 2.5}, zoom=4.5, size_max=40,
                         hover_name="region", color_continuous_scale="YlGn", map_style="carto-positron",
                         title=title, labels={"twh": f"Production ({UNIT})"})
    return fig.update_layout(height=500)


def small_multiples(by_region_year, title):
    fig = px.line(by_region_year, x="year", y="twh", color="region", facet_col="source", facet_col_wrap=2,
                  title=title, labels={"year": "Year", "twh": f"Production ({UNIT})", "region": "Region"})
    return fig.update_yaxes(matches=None).update_layout(height=600)
