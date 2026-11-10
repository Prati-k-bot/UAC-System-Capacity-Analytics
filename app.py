
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="UAC System Capacity & Care Load Analytics", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("UAC_Cleaned_Data.csv", parse_dates=["Date"])
    return df.sort_values("Date")

df = load_data()

st.title("📊 System Capacity & Care Load Analytics")
st.caption("Unaccompanied Children Care System | CBP and HHS operational analytics")

with st.sidebar:
    st.header("Filters")
    min_d, max_d = df["Date"].min().date(), df["Date"].max().date()
    date_range = st.date_input("Date range", (min_d, max_d), min_value=min_d, max_value=max_d)
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
        f = df[(df["Date"] >= start) & (df["Date"] <= end)].copy()
    else:
        f = df.copy()

if f.empty:
    st.warning("No data for the selected period.")
    st.stop()

latest = f.iloc[-1]
total_load = int(latest["Total System Load"])
net_pressure = int(latest["Net Intake Pressure"])
volatility = f["Total System Load"].std()
backlog_rate = (f["Net Intake Pressure"] > 0).mean() * 100
offset_ratio = f["Discharge Offset Ratio"].replace([np.inf, -np.inf], np.nan).mean() * 100

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Total Children Under Care", f"{total_load:,}")
c2.metric("Net Intake Pressure", f"{net_pressure:+,}")
c3.metric("Care Load Volatility", f"{volatility:,.0f}")
c4.metric("Backlog Accumulation Rate", f"{backlog_rate:.1f}%")
c5.metric("Discharge Offset Ratio", f"{offset_ratio:.1f}%")

st.divider()

tab1, tab2, tab3 = st.tabs(["System Overview", "Flow Analysis", "Detailed Data"])

with tab1:
    st.subheader("CBP vs HHS Care Load")
    melt = f[["Date","Children in CBP custody","Children in HHS Care"]].melt(
        id_vars="Date", var_name="System", value_name="Children"
    )
    fig = px.line(melt, x="Date", y="Children", color="System",
                  title="Care Load Trend", markers=False)
    fig.update_layout(legend_title_text="")
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        fig2 = px.line(f, x="Date", y="Total System Load",
                       title="Total System Load with 7-Day Average")
        fig2.add_scatter(x=f["Date"], y=f["7 Day Load Average"], mode="lines",
                         name="7-Day Average")
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        monthly = f.assign(Month=f["Date"].dt.to_period("M").astype(str)).groupby("Month", as_index=False)["Total System Load"].mean()
        fig3 = px.bar(monthly, x="Month", y="Total System Load", title="Average Monthly System Load")
        fig3.update_xaxes(tickangle=-45)
        st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.subheader("Intake, Transfers and Discharges")
    flow_cols = [app, trans, dis]
    fm = f[["Date"] + flow_cols].melt(id_vars="Date", var_name="Flow", value_name="Children")
    fig4 = px.line(fm, x="Date", y="Children", color="Flow", title="Daily Flow Trends")
    st.plotly_chart(fig4, use_container_width=True)

    fig5 = px.bar(f, x="Date", y="Net Intake Pressure",
                  title="Net Intake Pressure (Transfers − Discharges)")
    fig5.add_hline(y=0, line_dash="dash")
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Backlog / Stress Windows")
    stress = f[f["Backlog Flag"] == 1][["Date","Total System Load","Net Intake Pressure","7 Day Load Average"]]
    st.dataframe(stress.tail(100), use_container_width=True, hide_index=True)

with tab3:
    st.subheader("Operational Data")
    st.dataframe(f, use_container_width=True, hide_index=True)
    csv = f.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Download filtered data", csv, "UAC_filtered_data.csv", "text/csv")
