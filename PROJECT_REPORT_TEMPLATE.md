# EV Market Analysis Dashboard — Project Report Template

## 1. Title
EV Market Analysis Dashboard using Python and Streamlit

## 2. Abstract
This project presents an interactive web dashboard for exploring electric-vehicle market data. Users can filter records by year, manufacturer, and vehicle category, inspect sales trends, compare vehicle specifications, and calculate illustrative operating-cost and emissions differences under adjustable assumptions. Python is used for application logic, Pandas for data handling, Plotly for charts, and Streamlit for the web interface.

## 3. Problem Statement
EV information is spread across multiple sources and can be difficult for students to compare. A simple dashboard can place sales, vehicle specifications, and transparent comparison assumptions in one interface.

## 4. Objectives
- Build a simple interactive EV data dashboard.
- Visualize sales trends and manufacturer comparisons.
- Compare range, battery capacity, price, and charging time.
- Demonstrate a basic sustainability calculator.
- Allow filtered data to be downloaded as CSV.

## 5. Scope
The current version is an educational prototype using illustrative sample data. It demonstrates the workflow and UI; it is not a verified market-research system. Official data and citations should be added before making factual claims.

## 6. Tools and Technologies
- Python: core programming language
- Streamlit: web UI and interactive controls
- Pandas: loading, filtering, grouping, and aggregation
- Plotly Express: interactive visualizations
- CSV: simple dataset storage

## 7. System Architecture
CSV dataset → Pandas data loading/filtering → Streamlit controls and calculations → Plotly charts, KPI cards, tables, and CSV download.

## 8. Methodology
1. Store vehicle records in CSV format.
2. Load records into a Pandas DataFrame.
3. Let users select years, manufacturers, and categories.
4. Filter the DataFrame based on selections.
5. Calculate totals and averages.
6. Display the results as charts, metrics, and tables.
7. Export filtered records as CSV when requested.

## 9. Main Modules
### Module A: Market Overview
Displays total sample units sold, yearly trend, manufacturer sales, and vehicle category mix.

### Module B: Vehicle Comparison
Compares battery capacity, driving range, price, charging time, and sample sales.

### Module C: Sustainability
Calculates illustrative yearly emissions and running-cost differences from user-entered assumptions.

### Module D: Data Explorer
Displays filtered records and allows CSV download.

## 10. Limitations
- Sample records are illustrative, not official market statistics.
- Vehicle specifications and prices can vary by variant, year, test cycle, and region.
- Sustainability estimates depend on simplified assumptions and do not include full lifecycle impacts.
- The prototype does not include authentication, a database, or a live data API.

## 11. Future Scope
Use verified data sources, add geographical comparisons, integrate an official API where permitted, build a forecasting module with suitable historical data, and deploy the app online.

## 12. Conclusion
The project demonstrates how Python data tools can turn structured EV records into an interactive dashboard. It provides filtering, visualization, comparison, and export features suitable for a college demonstration. Reliable conclusions require replacing illustrative records with sourced data and documenting the source.

## 13. References to add before submission
List the exact dataset publisher, dataset title, publication/update date, URL, and access date for any real dataset used. Also cite official vehicle specification pages if individual model specifications are included.
