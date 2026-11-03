import numpy as np
import matplotlib.pyplot as plt

# 参数
fs = 1000
T = 1

# 时间轴
t = np.arange(0, T, 1/fs)
N = len(t)

# 产生混合信号：50 Hz 正弦波 (幅值 1.0) + 120 Hz 正弦波 (幅值 0.3)
# 注意：分量频率必须低于奈奎斯特频率 fs/2 = 500 Hz；
# 恰好等于 500 Hz 的正弦波采样点全落在零点上，等于不存在。
x = np.sin(2 * np.pi * 50 * t) + 0.3 * np.sin(2 * np.pi * 120 * t)

# FFT（rfft 只返回单边频谱，适合实信号）
X = np.fft.rfft(x)

# 频率轴
freq = np.fft.rfftfreq(N, d=1/fs)

# 幅值：先除以 N 归一化；单边频谱除 DC 与奈奎斯特分量外都要乘 2，才是真实幅值
amplitude = np.abs(X) / N
amplitude[1:-1] *= 2

# 绘图
plt.plot(freq, amplitude)
plt.title("FFT Spectrum (50 Hz + 120 Hz)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 200)
plt.grid()

plt.show()
