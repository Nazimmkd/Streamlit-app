import streamlit as st


def show(quality):
    st.subheader("Key insights")

    st.markdown("#### Insight 1 - Wind and solar drive the growth")
    st.markdown(
        "Between 2008 and 2025, solar production went from about 0.03 TWh to about 33 TWh, "
        "and wind from about 6 TWh to about 50 TWh. In 2025, total renewable electricity reaches "
        "about 148 TWh, roughly twice the 2008 level, and wind and solar represent more than half of it. "
        
    )

    st.markdown("#### Insight 2 - Each region has its own specialty")
    st.markdown(
        "In 2025, three regions lead the three main sources:\n"
        "- **Hydro**: Auvergne-Rhone-Alpes (about 24 TWh).\n"
        "- **Wind**: Hauts-de-France (about 12.5 TWh).\n"
        "- **Solar**: Nouvelle-Aquitaine (about 7.5 TWh).\n\n"
        "The map and the ranking show that no single region leads everything: "
        "production follows the local resources."
    )

    st.markdown("#### Insight 3 - Hydro is large but not stable")
    st.markdown(
        "Hydro is still the biggest single source, but it moves from year to year: "
        "it is lower in 2025 (about 57 TWh) than in 2024 (about 70 TWh). "
        "This is not necessarily a decline: hydro depends on rain and snow, "
        "and the last year may be provisional. Wind and solar, in contrast, grow almost every year."
    )

    st.subheader("Implications")
    st.markdown(
       
        "- **A more variable electricity mix.** Wind and solar depend on weather and daylight, "
        "so their growth makes production less predictable hour by hour. Storage and flexible grids become more important.\n"
        "- **Local planning.** Because specialties differ by region, local decision makers face different choices: "
        "wind farms in the north, solar in the south-west, maintenance of dams in the mountains.\n"
        "- **Do not read one year as a trend.** Especially for hydro, a single year can be higher or lower "
        "for weather reasons."
    )

    st.subheader("Next steps")
    st.markdown(
        "- Add **regional electricity consumption**, to see which regions produce more or less than they consume.\n"
        "- Add **population or area**, to compare regions fairly (production per inhabitant).\n"
        "- Add **renewable gas** once the missing years are available."
    )

    st.subheader("Data quality and limits")
    st.dataframe({name: [value] for name, value in quality.items()}, hide_index=True)
    st.info(
        "Limits: the file has no consumption, so we cannot compute a renewable share of consumption. "
        "Empty wind and bioenergy cells are treated as 0. Renewable gas is empty for some years (2014, 2025) "
        "and is not used here. Hydro varies with the weather, so a drop in one year is not a trend. "
        "The last year may be provisional. Regions are large areas: they hide differences inside each region."
    )
