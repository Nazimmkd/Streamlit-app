import streamlit as st

from utils.viz import area_chart


def show(df, tables):
    st.subheader("Wind and solar drive the growth")

    first, last = df["year"].min(), df["year"].max()
    national = tables["national"]
    total_first = national[national["year"] == first]["twh"].sum()
    total_last = national[national["year"] == last]["twh"].sum()
    wind_solar = national[(national["year"] == last) & national["source"].isin(["Wind", "Solar"])]["twh"].sum()
    top_region = tables["latest"].groupby("region")["twh"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(f"Production in {last}", f"{total_last:.0f} TWh", f"{total_last - total_first:+.0f} TWh vs {first}")
    col2.metric("Growth since first year", f"{(total_last / total_first - 1) * 100:+.0f} %")
    col3.metric("Wind + solar share", f"{wind_solar / total_last * 100:.0f} %",
                help="Share of wind and solar among the selected sources, in the last selected year.")
    col4.metric("Top region", top_region, help="Highest production in the last selected year.")

    st.plotly_chart(area_chart(national, "Renewable electricity production by source"), use_container_width=True)
    st.caption("Stacked areas: yearly production in TWh for each source, summed over the selected regions.")
