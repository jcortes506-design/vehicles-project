import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('./vehicles_us.csv')

st.header('Exploratory Data Analysis - Vehicles Dataset')

hist_buttom = st.button('Construir Histograma')
data = car_data[(car_data["price"] >= price_range[0]) & (car_data["price"] <= price_range[1])]
if hist_buttom:
    st.write('Creacion de un histograma para odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_buttom = st.button('Construir diagrama de dispersion')

if scatter_buttom:
    st.write('Creacion de un grafico de dispersion entre odometer y price')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

build_hist = st.checkbox("Mostrar histograma (odometer)")
if build_hist:
    st.write("Histograma de odometer")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
build_scatter = st.checkbox("Mostrar dispersion (odometer vs price)")



if build_scatter:
    st.write("Dispersion odometer vs price")
    fig = px.scatter(car_data, x="odometer", y="price",opacity=0.6)
    st.plotly_chart(fig, use_container_width=True)