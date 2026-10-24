# Renewable electricity in France - Data storytelling app (Streamlit)

**Question:** which renewable sources (hydro, bioenergy, wind, solar) grew between 2008 and 2025, in which regions, and how fast?

## Data
- File: `data/prod-region-annuelle-enr.csv` (yearly renewable production by region, in GWh, 13 regions, 2008-2025).
- Source and license: https://www.data.gouv.fr/datasets/production-regionale-annuelle-des-energies-renouvelables-2008-a-2021

- Units: the app shows TWh (1 TWh = 1000 GWh).

## Run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
If the CSV is missing, put it in `data/` or set `ENR_DATA_URL` to a direct link.

## Project structure
- `app.py`: page, sidebar filters, tabs
- `sections/`: the story (intro, overview, deep_dives, conclusions)
- `utils/io.py`: load data; `utils/prep.py`: cleaning and tables; `utils/viz.py`: charts

## Limitations
No consumption data, empty cells treated as 0, renewable gas not used (empty in some years), last year may be provisional, hydro depends on the weather.
