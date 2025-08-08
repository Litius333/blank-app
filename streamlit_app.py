import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Valdez_Enterprise', page_icon='Foto.png', layout='wide')

st.title("Proyecto : Protocolo Fantasma")

df = sns.load_dataset('tips')

with st.sidebar:

    select_sex = st.selectbox('Elegir:', df.sex.unique())

df.loc[df.sex == select_sex]

agree = st.checkbox("Generar grafico de densidad")
if agree:
    g = sns.displot(data = df.loc[df.sex == select_sex], x = 'total_bill',kind= 'kde')
    st.pyplot(g)

agree2 = st.checkbox("Generar grafico de barras smoker")
if agree2:
    f, ax = plt.subplots()
    ax = sns.barplot(data=df, x='sex', y='tip', hue='smoker')
    ax.set_title('Grafico promedio de Tips por fumador')
    st.pyplot(f)

agree3 = st.checkbox("Generar grafico de barras time")
if agree3:
    gh, ax =plt.subplots()
    ax = sns.barplot(data= df, y = df['total_bill'], x = 'sex', hue='time')
    st.pyplot(gh)

avg_bill_by_day = df.groupby(['day', 'sex'])['total_bill'].mean()

avg_tip_by_time = df.groupby('time')['tip'].mean()

with st.sidebar:

    tb1 = st.table(avg_tip_by_time)

    tb2 = st.table(avg_bill_by_day)