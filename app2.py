# Import the libraries
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Charts and Visualizations")

# Data
# Read a csv data, or Excel or maybe generate
@st.cache_data # Cache the data
def generate_data():
    dates = pd.date_range('2025-01-01', periods = 100)
    data = pd.DataFrame({
        'Date' : dates,
        'sales' : np.random.randn(100).cumsum() + 100,
        'profits' : np.random.rand(100).cumsum() + 50,
        'Customers' : np.random.randint(50, 200, 100) 
    })
    return data
data = generate_data()

# Graphs
# Line chart
st.subheader("Line Chart")
st.line_chart(data.set_index('Date')[['sales', 'profits']])

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(data.groupby(data['Date'].dt.month)['sales'].sum())
st.bar_chart(data.set_index('Date')[['sales', 'profits']])

# Area chart
st.subheader("Area Chart")
st.area_chart(data.set_index('Date')[['sales', 'profits']])

# Scatter plot
st.subheader("Scatter Plot")
chart_data = pd.DataFrame({
    "x" : np.random.randn(100),
    "y" : np.random.randn(100),
    'size' : np.random.randint(20, 100, 100)
})
st.scatter_chart(chart_data, x = 'x', y = 'y', size = 'size')

# Map 
st.subheader("Map")
map_data = pd.DataFrame({
    'lat' : np.random.normal(37.7749, 0.1, 100),
    'lon' : np.random.normal(-122.4194, 0.1, 100)
})
st.map(map_data)
