import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="EV Market Analysis", page_icon="🔋", layout="wide")

DATA_PATH = Path(__file__).parent / "data" / "electric_vehicles.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Year"] = df["Year"].astype(int)
    return df

df = load_data()

st.title("🔋 EV Market Analysis Dashboard")
st.caption("A beginner-friendly college project for exploring electric vehicle market trends.")
st.info("Demo note: The included dataset is illustrative sample data for demonstrating the dashboard. Do not present it as verified official market statistics.")

with st.sidebar:
    st.header("Filters")
    years = sorted(df["Year"].unique())
    selected_years = st.multiselect("Select year(s)", years, default=years)
    manufacturers = sorted(df["Manufacturer"].unique())
    selected_manufacturers = st.multiselect("Manufacturer(s)", manufacturers, default=manufacturers)
    categories = sorted(df["Vehicle_Type"].unique())
    selected_categories = st.multiselect("Vehicle type(s)", categories, default=categories)

filtered = df[
    df["Year"].isin(selected_years)
    & df["Manufacturer"].isin(selected_manufacturers)
    & df["Vehicle_Type"].isin(selected_categories)
].copy()

if filtered.empty:
    st.warning("No rows match these filters. Select at least one year, manufacturer, and vehicle type.")
    st.stop()

total_sales = int(filtered["Units_Sold"].sum())
avg_range = filtered["Range_km"].mean()
avg_battery = filtered["Battery_kWh"].mean()
market_revenue = (filtered["Units_Sold"] * filtered["Average_Price_INR"]).sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Units sold (sample)", f"{total_sales:,}")
c2.metric("Average range", f"{avg_range:.0f} km")
c3.metric("Average battery", f"{avg_battery:.1f} kWh")
c4.metric("Estimated revenue", f"₹{market_revenue / 10_000_000:.1f} Cr")

tab1, tab2, tab3, tab4 = st.tabs(["Market Overview", "Vehicle Comparison", "Sustainability", "Data Explorer"])

with tab1:
    st.subheader("Sales trend by year")
    sales_by_year = filtered.groupby("Year", as_index=False)["Units_Sold"].sum()
    st.plotly_chart(px.line(sales_by_year, x="Year", y="Units_Sold", markers=True,
                            title="Sample EV units sold by year"), use_container_width=True)

    left, right = st.columns(2)
    with left:
        by_maker = filtered.groupby("Manufacturer", as_index=False)["Units_Sold"].sum().sort_values("Units_Sold", ascending=False)
        st.plotly_chart(px.bar(by_maker, x="Manufacturer", y="Units_Sold", color="Manufacturer",
                               title="Units sold by manufacturer"), use_container_width=True)
    with right:
        by_type = filtered.groupby("Vehicle_Type", as_index=False)["Units_Sold"].sum()
        st.plotly_chart(px.pie(by_type, names="Vehicle_Type", values="Units_Sold",
                               title="Sales mix by vehicle type"), use_container_width=True)

with tab2:
    st.subheader("Compare EV specifications")
    comparison = filtered.groupby("Model", as_index=False).agg(
        Manufacturer=("Manufacturer", "first"),
        Vehicle_Type=("Vehicle_Type", "first"),
        Range_km=("Range_km", "mean"),
        Battery_kWh=("Battery_kWh", "mean"),
        Average_Price_INR=("Average_Price_INR", "mean"),
        Units_Sold=("Units_Sold", "sum"),
        Charging_Hours=("Charging_Hours", "mean"),
    )
    st.plotly_chart(px.scatter(comparison, x="Battery_kWh", y="Range_km", size="Units_Sold",
                               color="Manufacturer", hover_name="Model",
                               title="Battery capacity vs driving range",
                               labels={"Battery_kWh": "Battery capacity (kWh)", "Range_km": "Range (km)"}),
                    use_container_width=True)
    st.dataframe(comparison.sort_values("Range_km", ascending=False), use_container_width=True, hide_index=True)

with tab3:
    st.subheader("Illustrative sustainability estimates")
    st.caption("These estimates use simple assumptions for classroom demonstration, not measured lifecycle emissions.")
    km_per_year = st.slider("Assumed distance driven per vehicle per year (km)", 1000, 30000, 12000, 1000)
    ice_emissions_g_per_km = st.number_input("Assumed petrol vehicle emissions (g CO₂/km)", min_value=50, max_value=400, value=180, step=5)
    ev_emissions_g_per_km = st.number_input("Assumed EV electricity-related emissions (g CO₂/km)", min_value=0, max_value=250, value=60, step=5)
    ice_cost_per_km = st.number_input("Assumed petrol vehicle running cost (₹/km)", min_value=1.0, max_value=30.0, value=8.0, step=0.5)
    ev_cost_per_km = st.number_input("Assumed EV running cost (₹/km)", min_value=0.5, max_value=20.0, value=1.5, step=0.5)

    emissions_saved_kg = (ice_emissions_g_per_km - ev_emissions_g_per_km) * km_per_year / 1000
    annual_savings = (ice_cost_per_km - ev_cost_per_km) * km_per_year
    s1, s2 = st.columns(2)
    s1.metric("Estimated annual CO₂ difference", f"{emissions_saved_kg:,.0f} kg")
    s2.metric("Estimated annual running-cost difference", f"₹{annual_savings:,.0f}")
    st.write("**Interpretation:** Positive values indicate a lower estimated impact or cost for the EV under the assumptions entered. Actual results depend on electricity mix, vehicle efficiency, fuel prices, and driving conditions.")

with tab4:
    st.subheader("Filtered sample dataset")
    st.write(f"Showing **{len(filtered)}** records.")
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    csv_bytes = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download filtered data (CSV)", data=csv_bytes,
                       file_name="filtered_ev_market_data.csv", mime="text/csv")

st.divider()
st.subheader("Automatic insights")
best_range = filtered.loc[filtered["Range_km"].idxmax()]
best_sales = filtered.groupby("Manufacturer")["Units_Sold"].sum().idxmax()
st.markdown(f"- **Highest range in current selection:** {best_range['Model']} ({best_range['Range_km']} km).")
st.markdown(f"- **Highest sample sales by manufacturer:** {best_sales}.")
st.markdown(f"- **Models in current selection:** {filtered['Model'].nunique()}.")
st.caption("Project created for educational demonstration. Replace the sample CSV with a cited, reliable dataset before making real-world claims.")
