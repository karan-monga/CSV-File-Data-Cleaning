# CSV Data Cleaning & Standardization Demo

**Live App:** [https://csv-data-clean.streamlit.app/](https://csv-data-clean.streamlit.app/)

## 📌 Overview
This Streamlit app demonstrates practical data cleaning and standardization techniques for messy CSV files.  
It loads **transactions** and **complaints** data, fixes formatting issues, and prepares them for downstream analytics or AI/ML models.

## 🛠 Features
- Parse mixed date formats into consistent datetimes
- Normalize department names to a standard set
- Clean merchant and transaction IDs for reliable joins
- Convert various currency formats into USD floats
- Extract transaction IDs from free-text complaint descriptions
- Display raw vs cleaned datasets

## 🧹 Data Cleaning Techniques Used
- **Date Parsing:** Standardizing multiple date formats into uniform `datetime` objects using `pandas.to_datetime`.
- **Text Normalization:** Lowercasing, trimming whitespace, removing special characters, and mapping to canonical department names.
- **ID Standardization:** Removing spaces and normalizing case for merchant and transaction IDs.
- **Amount Standardization:** Converting currency strings with commas, decimals, and symbols into float USD values.
- **Regex Extraction:** Capturing transaction IDs from free-text complaint fields.
- **Vectorized Processing:** Using pandas operations for performance instead of Python loops.

## 📂 Data
Two sample CSV files are included:
- `transactions.csv` — structured transaction data
- `complaints.csv` — unstructured complaint records with messy formats

You can also upload your own CSVs via the sidebar.
