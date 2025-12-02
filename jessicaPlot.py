import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Espectro de Energia da Aceleração", layout="centered")
st.title("📈 Energia espectral da aceleração (FFT)")

st.write(
    """
    Carregue um arquivo de texto com duas colunas:
    - 1ª coluna: tempo (s)  
    - 2ª coluna: aceleração
    """
)

uploaded_file = st.file_uploader(
    "Selecione o arquivo (ex.: KINEM TO FIGURE.txt)",
    type=["txt", "csv"]
)

if uploaded_file is not None:
    # ---------------------------------------------------------
    # 1. Carregar dados
    # ---------------------------------------------------------
    try:
        data = np.loadtxt(uploaded_file)
    except Exception as e:
