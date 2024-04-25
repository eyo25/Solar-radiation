import streamlit as st
import pandas as pd
import plotly.express as px
# Function to load data
@st.cache
def load_data(file):
    return pd.read_csv(file)

st.title(" EDA Streamlit App")
st.title("solar Radation Data Analysis")
st.header("Upload your CSV data file")
# Function to load data from uploaded file
# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("Data loaded successfully!")
    
    # Sidebar for selecting analysis
    analysis_option = st.sidebar.selectbox(
        "Select Analysis",
        ("Time Series Analysis", "Correlation Analysis", "Wind Analysis", "Temperature Analysis", "Histograms", "Box Plots", "Scatter Plots")
    )

    if  analysis_option == "Summary Statistics":
        st.header("Summary Statistics")
        # Display statistical summary
        st.write("Statistical summary of numerical columns:")
        st.write(data.describe())

    elif analysis_option == "Time Series Analysis":
        st.header("Time Series Analysis")
        # Plot time series data
        st.write("Plotting GHI, DNI, DHI, and Tamb over time")
        fig = px.line(data, x='Timestamp', y=['GHI', 'DNI', 'DHI', 'Tamb'], title='Time Series Analysis')
        st.plotly_chart(fig)
        
    elif analysis_option == "Correlation Analysis":
        st.header("Correlation Analysis")
        # Calculate correlation matrix
        numeric_data = data.select_dtypes(include=['float64', 'int64'])
        corr_matrix = numeric_data.corr()
        # Plot correlation matrix
        st.write("Correlation Matrix")
        fig = px.imshow(corr_matrix, color_continuous_scale='RdBu_r')
        st.plotly_chart(fig)

    elif analysis_option == "Wind Analysis":
        st.header("Wind Analysis")
        # Plot wind data
        st.write("Plotting wind speed and direction over time")
        fig = px.line(data, x='Timestamp', y=['WS', 'WD'], title='Wind Analysis')
        st.plotly_chart(fig)

    elif analysis_option == "Temperature Analysis":
        st.header("Temperature Analysis")
        # Plot temperature data
        st.write("Plotting module temperatures and ambient temperature over time")
        fig = px.line(data, x='Timestamp', y=['TModA', 'TModB', 'Tamb'], title='Temperature Analysis')
        st.plotly_chart(fig)

    elif analysis_option == "Histograms":
        st.header("Histograms")
        # Plot histograms
        st.write("Histograms of GHI, DNI, DHI, WS, and temperatures")
        fig = px.histogram(data, x='GHI', title='Histogram of GHI')
        st.plotly_chart(fig)

    elif analysis_option == "Box Plots":
        st.header("Box Plots")
        # Plot box plots
        st.write("Box plots of GHI, DNI, DHI, WS, and temperatures")
        fig = px.box(data, y=['GHI', 'DNI', 'DHI', 'WS'], title='Box Plots')
        st.plotly_chart(fig)

    elif analysis_option == "Scatter Plots":
        st.header("Scatter Plots")
        # Plot scatter plots
        st.write("Scatter plots to explore relationships")
        fig = px.scatter(data, x='GHI', y='Tamb', title='GHI vs. Tamb')
        st.plotly_chart(fig)
 