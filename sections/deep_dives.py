import streamlit as st

from utils.viz import bar_chart, map_chart, small_multiples


def show(tables):
    last = tables["latest"]["year"].max()
    st.subheader("Where does the green electricity come from?")

    n = st.slider("Number of regions in the ranking", 3, 13, 6, help="The N regions with the highest production.")
    st.plotly_chart(bar_chart(tables["latest"], n, f"Top {n} regions in {last}, by source"), use_container_width=True)
    st.caption("Horizontal bars: production per region in TWh, split by source.")

    st.plotly_chart(map_chart(tables["latest"], f"Production by region in {last}"), use_container_width=True)
    st.caption("Bubble size and color show total production (TWh) in each region.")

    st.plotly_chart(small_multiples(tables["by_region_year"], "Each source, region by region"),
                    use_container_width=True)
    st.caption("One panel per source; each line is a region. Scales differ between panels.")
