# EV Market Analysis Dashboard

A beginner-friendly Streamlit web app for a college project. It explores electric-vehicle sales, specifications, and illustrative sustainability comparisons.

## Important data note
The included `data/electric_vehicles.csv` is **illustrative sample data created for this demonstration**. It is not an official dataset and must not be represented as verified market statistics. For a research submission, replace it with a trusted dataset and cite the source.

## Features
- Sidebar filters for year, manufacturer, and vehicle type
- KPI cards for units sold, average range, average battery capacity, and estimated revenue
- Yearly sales trend, manufacturer comparison, and vehicle-type mix charts
- Vehicle comparison table and battery-capacity vs range chart
- Adjustable, clearly labelled sustainability assumptions
- Filtered CSV download
- Automatic insights based on the selected sample records

## Requirements
- Python 3.10 or newer recommended
- Internet is needed only to install Python packages; the app runs locally after installation.

## Run on Windows
1. Install Python from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Extract this ZIP folder.
3. Open the project folder in VS Code.
4. Open Terminal > New Terminal.
5. Run:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
streamlit run app.py
```

6. Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## Run on macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

## Project modules
1. Data loading and preprocessing
2. Interactive market dashboard
3. EV specification comparison
4. Sustainability calculator
5. Data explorer and CSV export

## Suggested future improvements
- Replace demo data with official, cited EV registration/sales data
- Add state/city filters if the dataset includes location
- Add forecasting only after collecting a sufficiently large time series
- Add user login/database only if required by the college

## Troubleshooting
- `python is not recognized`: reinstall Python and enable PATH, or try `py` instead of `python`.
- `streamlit is not recognized`: activate the virtual environment and run `python -m streamlit run app.py`.
- Port busy: run `streamlit run app.py --server.port 8502`.
