# UAC System Capacity & Care Load Analytics

## Ready project contents
- `UAC_Cleaned_Data.csv` — cleaned dataset with derived analytics fields
- `app.py` — interactive Streamlit dashboard
- `requirements.txt` — Python dependencies
- `PowerBI_DAX_Measures.txt` — KPI measures for Power BI
- `KPI_Snapshot.csv` — calculated project KPI snapshot

## Dataset
Reporting period: 2023-01-12 to 2025-12-21
Rows after cleaning: 720

## Main KPIs
1. Total Children Under Care = CBP custody + HHS care
2. Net Intake Pressure = Transfers − Discharges
3. Care Load Volatility Index = population standard deviation of daily total load
4. Backlog Accumulation Rate = percentage of selected reporting days where transfers exceed discharges
5. Discharge Offset Ratio = total discharges / total transfers

## Run Streamlit
Open a terminal in this folder and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Power BI
1. Open Power BI Desktop.
2. Get Data → Text/CSV → `UAC_Cleaned_Data.csv`.
3. Confirm `Date` is Date type and numeric fields are Whole Number.
4. Create the measures in `PowerBI_DAX_Measures.txt`.
5. Add five Card visuals for the five main KPIs.
6. Add line charts for CBP vs HHS load and Net Intake Pressure.
7. Add a Date slicer.

## Suggested dashboard layout
Top row: five KPI cards.
Second row: CBP vs HHS Load Trend | Total System Load.
Third row: Net Intake Pressure | Intake/Transfer/Discharge flow.
Bottom row: monthly trend + detailed table.

## Important note
This is an analytics project based on the supplied dataset. KPI definitions are operational analytics definitions for this project and should not be treated as official HHS policy thresholds.
