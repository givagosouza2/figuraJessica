import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# 1. CARREGAR ARQUIVO
# ---------------------------------------------------------------------
# Arquivo com duas colunas: tempo (s) e aceleração
data = np.loadtxt("KINEM TO FIGURE.txt")  # ajuste o nome se necessário

t = data[:,0]    # tempo
a = data[:,1]    # aceleração

# ---------------------------------------------------------------------
# 2. CALCULAR FFT
# ---------------------------------------------------------------------
N = len(a)                 # número de amostras
dt = t[1] - t[0]           # intervalo temporal
Fs = 1/dt                  # frequência de amostragem
freqs = np.fft.rfftfreq(N, dt)

A_fft = np.fft.rfft(a)

# ---------------------------------------------------------------------
# 3. Converter amplitude para ENERGIA (densidade espectral)
# ---------------------------------------------------------------------
energy = np.abs(A_fft)**2 / N

# ---------------------------------------------------------------------
# 4. PLOTAR ESPECTRO DE ENERGIA
# ---------------------------------------------------------------------
plt.figure(figsize=(10,5))
plt.plot(freqs, energy, color='darkblue')
plt.xlabel("Frequência (Hz)")
plt.ylabel("Energia (|FFT|²)")
plt.title("Energia espectral da aceleração vs frequência\n(Transformada de Fourier)")
plt.grid(True)
plt.tight_layout()
plt.show()
