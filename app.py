import re
import numpy as np
import pandas as pd
import streamlit as st

# ------------------------
# Cleaning helper functions
# ------------------------

def clean_ids(s: str) -> str:
    if pd.isna(s):
        return np.nan
    return re.sub(r"\s+", "", str(s)).upper()

DEPT_MAP = {
    "ops": "Operations",
    "ops dept": "Operations",
    "operations": "Operations",
    "operations team": "Operations",
    "o p s": "Operations",
}

def normalize_department(s: str) -> str:
    if pd.isna(s):
        return np.nan
    s = str(s).strip().lower()
    s = re.sub(r"[^a-z ]+", "", s)         # remove punctuation/numbers
    s = re.sub(r"\s+", " ", s).strip()     # collapse spaces
    return DEPT_MAP.get(s, s.title())

def parse_any_date(s):
    return pd.to_datetime(s, errors="coerce", infer_datetime_format=True)

def parse_amount_to_dollars(s):
    if pd.isna(s):
        return np.nan
    x = str(s).strip()
    x = x.replace("$", "").replace("USD", "").strip()
    # handle European decimal comma
    if x.count(",") == 1 and x.count(".") == 0:
        x = x.replace(",", ".")
    # handle thousands separator
    if x.count(",") > 1 and "." in x:
        x = x.replace(",", "")
    try:
        return float(x)
    except:
        return np.nan

def extract_txn_id(text):
    if pd.isna(text):
        return np.nan
    t = str(text)
    m = re.search(r"(?:TXN[-\s]*|#|transaction\s+|txn[-\s]*)(\d{4,})", t, flags=re.I)
    if m:
        return m.group(1)
    m2 = re.search(r"(?<!\d)(\d{4,})(?!\d)", t)
    return m2.group(1) if m2 else np.nan

# ------------------------
# Streamlit UI setup
# ------------------------
st.set_page_config(page_title="Data Cleaning Demo")
st.title("Data Cleaning and Standardization")

# Upload or use local sample files
tx_file = st.sidebar.file_uploader("Upload transactions.csv", type=["csv"])
cp_file = st.sidebar.file_uploader("Upload complaints.csv", type=["csv"])

if tx_file:
    tx = pd.read_csv(tx_file, quotechar='"')
else:
    tx = pd.read_csv("transactions.csv", quotechar='"')

if cp_file:
    cp = pd.read_csv(cp_file, quotechar='"')
else:
    cp = pd.read_csv("complaints.csv", quotechar='"')

# ------------------------
# Raw preview
# ------------------------
st.subheader("Raw data preview")
st.write("Transactions")
st.dataframe(tx.head())
st.write("Complaints")
st.dataframe(cp.head())

# ------------------------
# Cleaning process
# ------------------------
st.subheader("Apply cleaning")

txc = tx.copy()
cpc = cp.copy()

# Standardize IDs
txc["merchant_id_std"] = txc["merchant_id"].apply(clean_ids)
cpc["merchant_id_std"] = cpc["merchant_id"].apply(clean_ids)

# Parse dates
txc["timestamp_parsed"] = parse_any_date(txc["timestamp"])
cpc["received_date_parsed"] = parse_any_date(cpc["received_date"])

# Standardize amounts
txc["amount_usd"] = (txc["amount_cents"] / 100.0).round(2)
if "amount" in cpc.columns:
    cpc["amount_usd"] = cpc["amount"].apply(parse_amount_to_dollars).round(2)

# Normalize departments
cpc["department_std"] = cpc["department_name"].apply(normalize_department)

# Extract transaction IDs from complaint text
cpc["transaction_id_extracted"] = cpc["complaint_text"].apply(extract_txn_id)

st.write("Cleaned Transactions")
st.dataframe(txc.head())
st.write("Cleaned Complaints")
st.dataframe(cpc.head())
