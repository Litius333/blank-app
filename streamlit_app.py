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

agrupar = df.groupby(['sex', 'day'])[['total_bill']].mean()
st.table(agrupar)

gh, ax =plt.subplots()
ax = sns.barplot(data= df, y = df['total_bill'], x = 'sex', hue='time')
st.pyplot(gh)

avg_bill_by_day = df.groupby(['day', 'sex'])['total_bill'].mean()
st.table(avg_bill_by_day)

avg_tip_by_time = df.groupby('time')['tip'].mean()
st.table(avg_tip_by_time)