import streamlit as st
import pandas as pd
import plotly.express as px
import glob
import os

# Set page title and wide layout
st.set_page_config(page_title="Regional Climate Dashboard", layout="wide")

st.title("🌍 Regional Climate Vulnerability Dashboard")
st.markdown("### Interactive analysis for Ethiopia's COP32 Position Paper")

# 1. DATA LOADING LOGIC
@st.cache_data
def load_data():
    # Looks for all cleaned files in the data directory
    all_files = glob.glob(os.path.join('data', "*_clean.csv"))
    all_data = []
    
    for filename in all_files:
        df = pd.read_csv(filename)
        # Extract country name from filename (e.g., 'nigeria' from 'data/nigeria_clean.csv')
        country_name = os.path.basename(filename).split('_')[0].capitalize()
        df['Country'] = country_name
        all_data.append(df)
    
    if not all_data:
        return pd.DataFrame()
    return pd.concat(all_data, ignore_index=True)

df_master = load_data()

# 2. SIDEBAR FILTERS (KPI Requirements)
st.sidebar.header("Dashboard Controls")

if not df_master.empty:
    # Country Selector
    all_countries = df_master['Country'].unique()
    selected_countries = st.sidebar.multiselect(
        "Select Countries to Compare", 
        options=all_countries, 
        default=list(all_countries)
    )

    # Year Range Slider
    min_year = int(df_master['YEAR'].min())
    max_year = int(df_master['YEAR'].max())
    year_range = st.sidebar.slider(
        "Select Year Range", 
        min_year, max_year, (min_year, max_year)
    )

    # Variable Selector
    target_var = st.sidebar.selectbox(
        "Select Climate Variable", 
        options=['T2M', 'PRECTOTCORR', 'T2M_MAX', 'T2M_MIN'],
        index=0
    )

    # Filter the data based on selection
    mask = (df_master['Country'].isin(selected_countries)) & \
           (df_master['YEAR'] >= year_range[0]) & \
           (df_master['YEAR'] <= year_range[1])
    filtered_df = df_master[mask]

    # 3. INTERACTIVE VISUALS
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"📈 {target_var} Trends Over Time")
        fig_line = px.line(
            filtered_df, 
            x='YEAR', 
            y=target_var, 
            color='Country',
            template="plotly_dark"
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        st.subheader(f"📊 {target_var} Distribution")
        fig_box = px.box(
            filtered_df, 
            x='Country', 
            y=target_var, 
            color='Country',
            template="plotly_dark"
        )
        st.plotly_chart(fig_box, use_container_width=True)

    # 4. SUMMARY STATS TABLE
    st.markdown("### Regional Summary Statistics")
    stats_df = filtered_df.groupby('Country')[target_var].agg(['mean', 'median', 'std']).round(2)
    st.table(stats_df)

else:
    st.error("No data found! Please check that your 'data/' folder contains your cleaned .csv files.")

st.info("💡 Pro Tip: Use the sidebar to zoom in on specific years or countries.")