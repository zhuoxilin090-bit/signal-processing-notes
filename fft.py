import numpy as np
import matplotlib.pyplot as plt

# 参数
fs = 1000
T = 1

# 时间轴
t = np.arange(0, T, 1/fs)
N = len(t)

# 产生 50 Hz 正弦波
x = np.sin(2 * np.pi * 100 * t) + 0.3 * np.sin(2 * np.pi * 500 * t)

# FFT
X = np.fft.rfft(x)

# 频率轴
freq = np.fft.rfftfreq(N, d=1/fs)

# 幅值
amplitude = np.abs(X) / N

# 绘图
plt.plot(freq, amplitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 100)
plt.grid()

plt.show()