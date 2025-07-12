import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Proyecto : Protocolo Fantasma")

df = sns.load_dataset('tips')

select_sex = st.selectbox('Elegir:', df.sex.unique())

df.loc[df.sex == select_sex]


agree = st.checkbox("Generar grafico de densidad")
if agree:
    g = sns.displot(data = df.loc[df.sex == select_sex], x = 'total_bill',kind= 'kde')
    st.pyplot(g)

agree2 = st.checkbox("Generar grafico de barras")
if agree2:
    f, ax = plt.subplots()
    ax = sns.barplot(data=df, x='sex', y='tip', hue='smoker')
    st.pyplot(f)