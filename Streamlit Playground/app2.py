import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Environment Info App')

@st.cache
def load_data():
    df = pd.read_csv("API_6_DS2_en_csv_v2_1232366.csv")
    return df
    
df=load_data()

years=[]
for col in df.columns:
    if col.isnumeric():
        years.append(col)

st.sidebar.title("Filter data")
     
countriesSelected = st.sidebar.multiselect('Select countries',  df["Country Name"].unique())        
indicator_list = st.sidebar.selectbox("Select Indicator", df["Indicator Name"].unique())
years_list = st.sidebar.slider("Select Year", 1960,2019)
#values=df.loc[(df["Indicator Name"] == indicator_list), str(years_list)]

#mask_countries = df['Country Name'].isin(COUNTRIES_SELECTED)

values=df.loc[(df["Indicator Name"] == indicator_list) & (df['Country Name'].isin(countriesSelected)), str(years_list)]
st.subheader(indicator_list)


plot = pd.DataFrame({
  'countries': countriesSelected,
  'values': values
})
plot = plot.set_index('countries')
'''### RAW DATA'''
plot
'''### LINE CHART'''
st.line_chart(plot)
'''### AREA CHART'''
st.area_chart(plot)
'''### Bar Chart'''
st.bar_chart(plot)