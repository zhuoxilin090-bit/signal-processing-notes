import matplotlib.pyplot as plt
import numpy as np

# --- 1. 参数设定 ---
Fs = 1000  # 采样频率：1000 Hz
T = 1.0  # 观察时间：1 秒
N = int(Fs * T)  # 总采样点数：1000 点

t = np.linspace(0, T, N, endpoint=False)

# --- 2. 构造混合信号：50 Hz (幅值1.0) + 120 Hz (幅值0.5) ---
f1, A1 = 50, 1.0
f2, A2 = 120, 0.5
f3, A3=300,0.8
y = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t) + A3 * np.sin(2 * np.pi * f3 * t)

# --- 3. 核心步骤：执行 FFT 变换 ---
Y_fft = np.fft.fft(y)  # 计算出来的是 N 个复数

# 计算对应的频率横坐标 (0 到 Fs)
freqs = np.fft.fftfreq(N, d=1 / Fs)

# --- 4. 转换幅值：归一化与单边频谱 ---
# 复数取模，除以 N 进行能量归一化
amplitude = np.abs(Y_fft) / N

# FFT 结果是双边的（包含正频率和负频率镜像），我们取前一半（单边频谱）
half_N = N // 2
freqs_single = freqs[:half_N]
amplitude_single = amplitude[:half_N] * 2  # 单边能量要乘以 2 (DC分量除外)

# --- 5. 可视化 ---
plt.figure(figsize=(10, 5))

# 子图 1：时域混合波形
plt.subplot(2, 1, 1)
plt.plot(t[:400], y[:400], "b-")  # 仅画前 0.2 秒，看清波形
plt.title("Time Domain: Mixed Signal (50 Hz + 120 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# 子图 2：频域频谱图 (Spectrum)
plt.subplot(2, 1, 2)
plt.plot(freqs_single, amplitude_single, "r-", linewidth=1.5)
plt.title("Frequency Domain: FFT Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0, 400)  # 只观察 0-200 Hz 区间
plt.grid(True)

plt.tight_layout()
plt.show()