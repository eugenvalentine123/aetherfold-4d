import streamlit as st
pip install --upgrade pip
import numpy as np
import pandas as pd
import plotly.express as px

# Title of the app
st.title('AetherFold 4D Visualization App')

# Upload file section
uploaded_file = st.file_uploader('Upload your data file (CSV)', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('Data successfully loaded!')
    st.write(df.head())

    # 4D Visualization section
    st.subheader('4D Visualization')
    if 'x' in df.columns and 'y' in df.columns and 'z' in df.columns and 'color' in df.columns:
        fig = px.scatter_3d(df, x='x', y='y', z='z', color='color', size='size', hover_name='name')
        st.write(fig)
    else:
        st.warning('Data requires x, y, z, color, and size columns for visualization.')

    # Analytics section
    st.subheader('Analytics Dashboard')
    st.write('Summary Statistics:')
    st.write(df.describe())

    # Download functionality
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)
    st.download_button(
        label='Download data as CSV',
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )
else:
    st.info('Awaiting CSV file upload...')

# Footer
st.markdown("---")
st.markdown("### AetherFold 4D Visualization App")
st.markdown("Developed by eugenvalentine123" )
