import pandas as pd
import streamlit as st
import numpy as np
import pickle
from PIL import Image

image = Image.open('img/casa_ap.jpg')
image_logo = Image.open('img/predict_r.png')

st.header('Previsão de Preços - Casas e Apartamentos')

#st.text('Cidades: Belo Horizonte, Rio de Janeiro e São Paulo')

st.write("""Previsão de Preços - Casas e Apartamentos para as **Cidades**:\n 
**Belo Horizonte, Rio de Janeiro e São Paulo**.""")

st.image(image)
st.sidebar.image(image_logo)


st.sidebar.title('Predict')
st.sidebar.markdown("##### *Preencha os campos abaixo para realizar a Previsão*.")
tipo = st.sidebar.radio('Tipo',('Casa','Apartamento'))
cidade = st.sidebar.selectbox('Cidade', ['Belo Horizonte', 'São Paulo', 'Rio de Janeiro'])
quartos = st.sidebar.number_input("Quartos", 0,10)
suite = st.sidebar.number_input("Suites", 0,10)
banheiro = st.sidebar.number_input("Banheiros", 0,10)
garagem = st.sidebar.number_input("Garagem", 0,10)
elevador = st.sidebar.radio('Elevador',('Sim','Não'))
metro_trem = st.sidebar.radio('Próximo Metro/Trem',('Sim','Não'))
area = st.sidebar.slider('Area',1,1000)

condominio = st.sidebar.text_input("Valor Condominio",0)
iptu = st.sidebar.text_input("Valor IPTU",0)



if tipo == 'Casa':
    casa = 1
    apartamento = 0

elif tipo == 'Apartamento':
    casa = 0
    apartamento = 1

if elevador == 'Sim':
    elevador = 1
else:
    elevador = 0


if metro_trem == 'Sim':
    metro_trem = 1
else:
    metro_trem = 0

if cidade == 'Belo Horizonte':
    cidade_bh = 1
    cidade_rio = 0
    cidade_sp = 0

elif cidade == 'São Paulo':
    cidade_bh = 0
    cidade_rio = 0
    cidade_sp = 1

elif cidade == 'Rio de Janeiro':
    cidade_bh = 0
    cidade_rio = 1
    cidade_sp = 0

lista = np.array([[area, quartos, suite, banheiro, garagem, elevador, metro_trem, condominio, iptu, apartamento, casa, cidade_bh, cidade_rio, cidade_sp]])


with open('Modelo/Modelo_RF.pkl','rb') as f:
  model = pickle.load(f)

modelo = model.predict(lista)[0]

st.markdown(
        f'<div <br></div>',
        unsafe_allow_html=True)



st.write("#### O valor previsto para {} em {} é de:".format(tipo, cidade))
#st.markdown("## R$ {:,}".format(round(modelo,2)))
#aa = print("R$ {:,}".format(round(modelo,2)))
#if st.sidebar.button('Predict'):
st.markdown(
            f'<div style="color: blue; font-size: 60px">{"R$ {:,}".format(round(modelo,2))}</div>',
            unsafe_allow_html=True)