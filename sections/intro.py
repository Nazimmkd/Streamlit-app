import streamlit as st

from utils.io import LICENSE, SOURCE


def show():
    st.header("France's renewable electricity: a quiet revolution")

    st.markdown("#### Why it matters")
    st.markdown(
        "In less than 20 years, wind and solar went from almost nothing to major electricity sources. "
        "In this dataset, wind production grew from about 6 TWh in 2008 to about 50 TWh in 2025, "
        "and solar from almost zero (0.03 TWh) to about 33 TWh. "
        "Together they now make up more than half of the renewable electricity produced in France. "
        "This change affects how electricity is produced, where it is produced, and what the power grid "
        "must handle in the future."
    )

    st.markdown("#### Context")
    st.markdown(
        "The data gives the yearly renewable electricity production of each French region, from 2008 to 2025. "
        "Four sources are covered: **hydro** (dams and rivers), **bioenergy** (biomass and biogas), "
        "**wind** and **solar**. Hydro has been used for a long time and depends on the weather, "
        "while wind and solar are recent and growing quickly."
    )

    st.markdown("#### The questions of this dashboard")
    st.markdown(
        "1. How much renewable electricity does France produce, and how has it changed since 2008?\n"
        "2. Which sources are driving this growth?\n"
        "3. Which regions produce the most, and with which source?\n\n"
      
    )

    st.markdown("#### How to read this dashboard")
    st.markdown(
        "- **Overview**: key numbers and the evolution of production by source.\n"
        "- **Deep dives**: ranking of regions, map, and each source region by region.\n"
        "- **Conclusions**: main insights, next steps, and the limits of the data.\n\n"
       
    )

    with st.expander("Units and definitions"):
        st.markdown(
            "- **GWh / TWh**: units of energy. 1 TWh = 1,000 GWh = one billion kWh. The app shows TWh.\n"
            "- **Production**: electricity produced in a region during one year, not consumption.\n"
            "- **Wind + solar share**: wind and solar production divided by the production of all selected sources."
        )

    st.caption(f"Source: {SOURCE} | License: {LICENSE}")
