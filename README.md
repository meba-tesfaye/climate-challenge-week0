# Climate Challenge Week 0 
## Environment Setup 
1. Clone the repository 
2. Create virtual environment: `py -m venv venv` 
3. Activate environment: `venv\Scripts\activate` 
4. Install dependencies: `pip install -r requirements.txt` 
## 📊 Project Overview
This project performs an extensive **Exploratory Data Analysis (EDA)** on climate data for five African nations (Kenya, Sudan, Tanzania, Ethiopia, and Nigeria) from 2015 to 2026. The goal is to identify patterns in temperature, humidity, and rainfall to support agricultural and environmental planning.

## 🛠️ Data Science Stack
I utilized the following libraries to process and visualize the climate datasets:

* **Pandas:** For cleaning NASA POWER data and managing time-series structures.
* **Seaborn:** For statistical visualizations like Box Plots and Heatmaps.
* **Matplotlib:** For custom plotting, secondary axes, and figure styling.
* **NumPy:** For handling numerical arrays and climate metric calculations.

## 📈 Analysis Coverage
For each country, the following insights were generated:
* **Temperature Distributions** (Histograms & Box Plots)
* **Climate Correlations** (Heatmaps)
* **Seasonal Trends** (Time-series Line Graphs)
* **Rainfall Intensity** (Bubble Charts)# African Climate Resilience Dashboard (COP32)

A data-driven analysis of climate trends across Ethiopia, Sudan, Kenya, Tanzania, and Nigeria. Developed as part of the 10 Academy Climate Challenge.

## 🚀 Project Overview
This project analyzes 30+ years of NASA POWER data to identify climate vulnerabilities. It includes:
* **Exploratory Data Analysis:** Temperature trends and precipitation variability.
* **Statistical Rigor:** ANOVA testing to confirm regional climate differences.
* **Extreme Event Tracking:** Visualization of heat stress (>35°C) and drought spells.
* **Interactive Dashboard:** A Streamlit application for real-time data exploration.

## 📁 Project Structure
* `app/`: Streamlit dashboard code (`main.py`).
* `notebooks/`: Detailed EDA for each country and the final comparison.
* `scripts/`: Support documentation and utility scripts.
* `data/`: (Local) NASA POWER climate datasets.

## 🛠️ Installation & Usage
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run app/main.py`
