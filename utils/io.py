"""Load the data: use the local file, or download it once if it is missing."""
import os
from pathlib import Path

import pandas as pd
import requests

RAW_FILE = Path(__file__).resolve().parent.parent / "data" / "prod-region-annuelle-enr.csv"
DATA_URL = os.environ.get("ENR_DATA_URL", "")  # optional: direct link to the CSV

SOURCE = "https://www.data.gouv.fr/datasets/production-regionale-annuelle-des-energies-renouvelables-2008-a-2021"
LICENSE = "LICENSE OUVERTE / Open License version 2.0"


def load_data():
    if not RAW_FILE.exists():
        if not DATA_URL:
            raise FileNotFoundError("Put the CSV in data/ or set ENR_DATA_URL")
        RAW_FILE.parent.mkdir(exist_ok=True)
        response = requests.get(DATA_URL, timeout=120)
        response.raise_for_status()
        RAW_FILE.write_bytes(response.content)
    return pd.read_csv(RAW_FILE, sep=";", encoding="utf-8-sig", usecols=lambda c: c != "Géo-shape région")
