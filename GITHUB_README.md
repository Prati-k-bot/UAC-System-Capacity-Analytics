# System Capacity & Care Load Analytics for Unaccompanied Children

## Project Overview
This project develops an analytics framework for monitoring system capacity and care load across the U.S. Unaccompanied Children (UAC) care pipeline using operational time-series data.

The analysis focuses on:
- CBP custody load
- Transfers from CBP into the HHS care system
- HHS care load
- HHS discharges
- Total system load
- Net intake pressure
- Care-load volatility
- Backlog accumulation
- Discharge offset

## Objectives
1. Quantify daily and cumulative care load.
2. Compare CBP and HHS care loads.
3. Identify periods of increasing or decreasing system pressure.
4. Monitor the balance between transfers and discharges.
5. Provide interactive analytics through Power BI and Streamlit.

## Dataset
The supplied dataset contains operational reporting records with:
- Date
- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care

## Derived Metrics
### Total System Load
CBP Custody + HHS Care

### Net Intake Pressure
Transfers into HHS − Discharges from HHS

### Care Load Volatility Index
Standard deviation of daily total system load.

### Backlog Accumulation Rate
Percentage of selected reporting days where transfers exceed discharges.

### Discharge Offset Ratio
Total HHS discharges / total transfers into HHS.

## Technologies
- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Power BI
- DAX

## Streamlit Application
The Streamlit dashboard provides:
- Date range filtering
- KPI cards
- CBP vs HHS trend analysis
- Total system load trend
- Intake/transfer/discharge analysis
- Net intake pressure
- Backlog/stress-period analysis
- Detailed data table
- CSV download

## Project Structure
```text
UAC-System-Capacity-Analytics/
│
├── app.py
├── UAC_Cleaned_Data.csv
├── KPI_Snapshot.csv
├── PowerBI_DAX_Measures.txt
├── requirements.txt
└── README.md
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Disclaimer
This is an academic analytics project based on the supplied dataset. The KPI definitions and analytical thresholds are project-level definitions and should not be interpreted as official government policy thresholds.
