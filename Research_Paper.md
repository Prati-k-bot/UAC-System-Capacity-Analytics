SYSTEM CAPACITY & CARE LOAD ANALYTICS FOR UNACCOMPANIED CHILDREN

Abstract
This project presents a data analytics framework for monitoring system capacity and care load in the Unaccompanied Children (UAC) care pipeline. The supplied operational time-series dataset contains daily observations related to children entering CBP custody, children remaining in CBP custody, transfers into the HHS care system, children in HHS care, and children discharged from HHS care. The project transforms these operational measures into interpretable indicators including Total System Load, Net Intake Pressure, Care Load Volatility Index, Backlog Accumulation Rate, and Discharge Offset Ratio. Interactive dashboards are developed using Power BI and Streamlit to support trend analysis, monitoring, and data-driven operational awareness.

Keywords
UAC, healthcare analytics, capacity analytics, time-series analysis, Power BI, Streamlit, Python, operational dashboard, care load.

1. INTRODUCTION
Large-scale care systems require continuous visibility into the number of people under responsibility, movement through the system, and changes in demand and discharge. The UAC care pipeline includes intake into CBP custody, transfer to HHS care, provision of care and services, and eventual discharge to vetted sponsors or other appropriate outcomes.

Operational data can be difficult to interpret when individual measures are viewed separately. This project combines these measures into a centralized analytical framework. The objective is not to create a policy decision, but to provide transparent descriptive analytics that can help stakeholders understand system load and changes over time.

2. PROBLEM STATEMENT
A care system can experience increased operational pressure when incoming transfers remain above outgoing discharges for sustained periods. Similarly, large changes in the active population can create planning challenges. Without integrated visualization, it is difficult to identify these patterns quickly.

The project therefore addresses the following questions:
1. What is the current system-wide care load?
2. How does CBP custody compare with HHS care load?
3. What is the balance between transfers and discharges?
4. When does sustained positive net intake occur?
5. How variable is the overall care load?
6. How can these indicators be presented through an interactive dashboard?

3. OBJECTIVES
Primary objectives:
- Quantify daily system-wide care load.
- Compare CBP and HHS active care loads.
- Analyze transfers and discharges.
- Identify periods of sustained positive net intake.
- Visualize operational trends.

Secondary objectives:
- Provide a reusable dashboard framework.
- Support exploratory capacity monitoring.
- Make the analysis understandable through KPI cards and charts.
- Provide both Power BI and Streamlit implementations.

4. DATASET DESCRIPTION
The dataset contains reporting-date observations and five operational measures:
- Date
- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care

The data was converted into appropriate date and numeric types. Blank rows were removed and records were ordered chronologically.

5. DATA PREPROCESSING
The preprocessing workflow consisted of:
1. Loading the CSV dataset.
2. Removing completely blank records.
3. Converting Date into datetime format.
4. Removing commas from numeric values.
5. Converting operational fields to numeric types.
6. Sorting records chronologically.
7. Removing duplicate dates where required for the analytical table.
8. Creating derived metrics.

6. FEATURE ENGINEERING
6.1 Total System Load
Total System Load = Children in CBP custody + Children in HHS Care

This represents the combined active care responsibility across the two stages represented in the dataset.

6.2 Net Intake Pressure
Net Intake Pressure = Children transferred out of CBP custody − Children discharged from HHS Care

A positive value means transfers exceeded discharges for that reporting day. A negative value means discharges exceeded transfers.

6.3 Care Load Growth Rate
Care Load Growth Rate is calculated as the day-over-day percentage change in Total System Load.

6.4 Rolling Averages
Seven-day and fourteen-day rolling averages are calculated to reduce the effect of short-term fluctuations and make broader trends easier to observe.

6.5 Backlog Indicator
A project-level backlog indicator is created when the seven-day average of Net Intake Pressure remains positive. This is an analytical indicator rather than an official operational definition.

6.6 Discharge Offset Ratio
Discharge Offset Ratio = Total HHS Discharges / Total Transfers into HHS

A ratio near 1 indicates that aggregate discharges are close to transfers for the selected period.

7. EXPLORATORY DATA ANALYSIS
The dashboard examines:
- Daily care-load trends.
- CBP versus HHS load.
- Daily transfers and discharges.
- Net intake pressure.
- Monthly average system load.
- Rolling load averages.
- Periods associated with positive net intake.

The analysis is descriptive. It does not infer individual-level outcomes or make policy recommendations.

8. KPI FRAMEWORK
KPI 1: Total Children Under Care
Measures the active combined CBP and HHS care load for the selected/latest reporting context.

KPI 2: Net Intake Pressure
Measures the difference between transfers into HHS and HHS discharges.

KPI 3: Care Load Volatility Index
Uses the standard deviation of daily total system load to describe variability.

KPI 4: Backlog Accumulation Rate
Measures the percentage of selected reporting days on which transfers exceed discharges.

KPI 5: Discharge Offset Ratio
Compares total discharges with total transfers.

9. POWER BI DASHBOARD
The Power BI dashboard contains five KPI cards at the top. Supporting visuals include:
- CBP vs HHS care-load line chart.
- Total system-load trend.
- Intake, transfer and discharge trend.
- Net intake pressure chart.
- Monthly system-load analysis.
- Date slicer.
- Detailed operational table.

The DAX measures are included with the project package.

10. STREAMLIT APPLICATION
The Streamlit application provides an interactive web interface. Users can select a date range and inspect KPI cards and trend charts. The application also provides a detailed data table and CSV download option.

Main technologies:
- Streamlit for the web interface.
- Pandas for data processing.
- NumPy for calculations.
- Plotly for interactive charts.

11. SYSTEM ARCHITECTURE
Data Source
    ↓
CSV Ingestion
    ↓
Data Cleaning & Validation
    ↓
Feature Engineering
    ↓
KPI Calculation
    ↓
Power BI / Streamlit Dashboard
    ↓
Interactive Visualization & Analysis

12. RESULTS AND INSIGHTS
The framework converts raw daily operational measurements into a structured monitoring dashboard. It makes it possible to inspect changes in active system load, compare the two care stages, and identify periods when transfers exceed discharges.

The dashboard is designed so that users can change the reporting period and observe how KPI values and trends change.

13. LIMITATIONS
- The dataset contains reporting observations rather than a complete individual-level case history.
- Missing reporting dates may occur because the source does not necessarily provide an observation for every calendar day.
- The backlog and volatility measures are project-defined analytical indicators.
- No causal conclusions are drawn from the time-series relationships.
- Dashboard results depend on the quality and completeness of the supplied dataset.

14. FUTURE ENHANCEMENTS
Future versions could include:
- Forecasting of system load using time-series models.
- Automated anomaly detection.
- Capacity thresholds when an official capacity dataset is available.
- Additional regional or facility-level data.
- Automated data refresh.
- Role-based dashboards.
- Alert notifications for sustained changes.

15. CONCLUSION
This project provides a practical analytics framework for understanding care-system load and operational flows in the UAC pipeline. By combining data preprocessing, feature engineering, KPI analysis, Power BI visualization, and Streamlit deployment, the project transforms raw operational data into an accessible analytical dashboard. The framework can be extended with forecasting, anomaly detection, and additional capacity information.

REFERENCES / DATA SOURCE
The project uses the dataset supplied with the Unified Mentor project instructions. Background context can be cross-checked against the U.S. Department of Health and Human Services UAC program information and the project documentation supplied by Unified Mentor.
