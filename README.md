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

## 📂 Data  
Two sample CSV files are included:  
- `transactions.csv` — structured transaction data  
- `complaints.csv` — unstructured complaint records with messy formats  

You can also upload your own CSVs via the sidebar.  
