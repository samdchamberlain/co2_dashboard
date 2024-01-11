import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from typing import Optional
from load_data import load_raw_data_to_df


@st.cache_data
def get_data(freq: Optional[int] = None) -> pd.DataFrame:
    # Load from local file or, if frequency supplied, we rebuild the clean_data.csv
    if not freq:
        return pd.read_csv('data/clean_data.csv')
    return load_raw_data_to_df(freq)

df = get_data()

col1, col2 = st.columns(2)
with col2:
    freq = st.number_input("Aggregate frequency", value=3600, placeholder="Type an int to agg the raw data by...")
with col1:
    st.write('Default agg frequency for raw data is ', freq)
    if st.button('Reload Raw Data'):
        st.markdown("Reloading data from raw file...")
        df = get_data(freq)

values = st.slider(
    'Select a range of values (most recent half of data by default)',
    0.0, df.timestamp.max(),
    (np.floor(df.timestamp.max()*.50), df.timestamp.max())
)
plot_df = df[df.timestamp.between(values[0], values[1])].copy()

tab1, tab2, tab3 = st.tabs(["CO2", "Temp", "RH"])

with tab1:
    fig1 = px.line(plot_df, x="timestamp", y="co2", title='CO2 (ppm)')
    st.write(fig1)

with tab2:
    fig1 = px.line(plot_df, x="timestamp", y="temp", title='Temp')
    st.write(fig1)

with tab3:
    fig3 = px.line(plot_df, x="timestamp", y="rh", title='RH')
    st.write(fig3)