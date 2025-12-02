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
        st.error(f"Erro ao ler o arquivo: {e}")
    else:
        if data.shape[1] < 2:
            st.error("O arquivo precisa ter pelo menos duas colunas: tempo e aceleração.")
        else:
            t = data[:, 0]
            a = data[:, 1]

            # ---------------------------------------------------------
            # 2. FFT
            # ---------------------------------------------------------
            N = len(a)
            dt = t[1] - t[0]  # supõe amostragem uniforme
            Fs = 1.0 / dt

            freqs = np.fft.rfftfreq(N, dt)
            A_fft = np.fft.rfft(a)

            # Energia espectral (proporcional a |FFT|²)
            energy = np.abs(A_fft) ** 2 / N

            st.write(f"**Número de amostras (N):** {N}")
            st.write(f"**Frequência de amostragem estimada (Fs):** {Fs:.2f} Hz")

            # ---------------------------------------------------------
            # 3. Gráfico Energia × Frequência (0–20 Hz)
            # ---------------------------------------------------------
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(freqs, energy)
            ax.set_xlim(0, 20)  # limite superior 20 Hz
            ax.set_xlabel("Frequência (Hz)")
            ax.set_ylabel("Energia (|FFT|²)")
            ax.set_title("Energia espectral da aceleração vs frequência (FFT)\n(Limite superior = 20 Hz)")
            ax.grid(True)

            st.pyplot(fig)
else:
    st.info("👉 Aguarde o upload de um arquivo para ver o gráfico.")
