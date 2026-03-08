import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In search for Happiness")

select_box = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))

select__box = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f" {select_box} and {select__box}")

df = pd.read_csv("happy.csv")

match select_box:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]
match select__box:
    case "GDP":
        y_array = df["gdp"]

    case "Happiness":
        y_array = df["happiness"]

    case "Generosity":
        y_array = df["generosity"]

figure = px.scatter(x=x_array, y=y_array , labels={"x": select_box, "y": select__box})                     #plotly data frame for  graphs
st.plotly_chart(figure)