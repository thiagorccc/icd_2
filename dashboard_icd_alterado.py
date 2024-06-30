#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:52:15 2024

@author: thiagocosta
"""



import streamlit as st
import plotly.express as px
import pandas as pd
import json
from urllib.request import urlopen
from PIL import Image

dados = pd.read_excel('resultados 2.xlsx')
result_ch = pd.read_excel('resultados_ch.xlsx')
result_kmeans = pd.read_excel('resultados_kmeans.xlsx')
ranking = pd.read_excel('ranking.xlsx')

#%%
# Configurar a página do Streamlit
st.set_page_config(page_title="Resultados", layout="wide")

# importing .json file and checking it
with urlopen('https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-35-mun.json') as response:
    geo_json_sp = json.load(response)

# Criar o mapa coroplético
fig_kmeans2 = px.choropleth_mapbox(
    dados,
    geojson=geo_json_sp,
    locations='id',
    featureidkey="properties.id",
    color='grupo_k2',
    hover_data={'cidades': True, 'idhm': True,'alta_tecnologia': True, 'media_alta_tecnologia': True, 'media_tecnologia': True, 'media_baixa_tecnologia': True},
    color_continuous_scale=px.colors.sequential.Blues,  # Paleta de cores sequencial
    mapbox_style="carto-positron",
    zoom=5,
    center={"lat": -23.55, "lon": -46.63},
    opacity=0.5
)

# Criar o mapa coroplético
fig_ch2 = px.choropleth_mapbox(
    dados,
    geojson=geo_json_sp,
    locations='id',
    featureidkey="properties.id",
    color='grupo_ward_2',
    hover_data={'cidades': True, 'idhm': True,'alta_tecnologia': True, 'media_alta_tecnologia': True, 'media_tecnologia': True, 'media_baixa_tecnologia': True},
    color_continuous_scale='Viridis',  # Paleta de cores sequencial
    mapbox_style="carto-positron",
    zoom=5,
    center={"lat": -23.55, "lon": -46.63},
    opacity=0.5
)

# Exibir o mapa no Streamlit
st.title("K Means (k=2)")
st.subheader("Distribuição Geográfica")
st.plotly_chart(fig_kmeans2)
st.subheader("Média dos Grupos")
st.dataframe(result_kmeans)

st.title("Cluster Hierárquico (k=2)")
st.subheader("Distribuição Geográfica")
st.plotly_chart(fig_ch2)
st.subheader("Média dos Grupos")
st.dataframe(result_ch)

st.title("Principal Component Analysis (PCA)")
st.subheader("Gráficos")

col1, col2 = st.columns(2)

with col1:
    pca_fig = Image.open("pca.png")
    width, height = pca_fig.size
    pca_fig = pca_fig.resize((width // 4, height // 4))
    st.image(pca_fig)

with col2:
    fatores_fig = Image.open("fatores.png")
    width, height = pca_fig.size
    fatores_fig = fatores_fig.resize((width // 1, height // 1))
    st.image(fatores_fig)  


st.subheader("Ranking")
st.dataframe(ranking)

st.title("Árvore de Decisão")
cart_fig = Image.open("Arvore Teste.png")
st.image(cart_fig)

