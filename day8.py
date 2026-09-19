import matplotlib.pyplot as plt
import numpy as np

# --- 1. 参数设置 ---
Fs = 1000  # 采样率
T = 1.0  # 采样时间 1秒
N = int(Fs * T)

t = np.linspace(0, T, N, endpoint=False)

# 构造一个非整数周期的信号 (50.3 Hz)
f_signal = 50.3
y = np.sin(2 * np.pi * f_signal * t)

# --- 2. 矩形窗 (未加窗/原始截断) vs 汉宁窗 (Hanning Window) ---
# 汉宁窗
win_hanning = np.hanning(N)
y_windowed = y * win_hanning

# --- 3. 计算 FFT 并归一化 ---
# 未加窗 FFT
Y_raw = np.fft.fft(y) / N
# 加窗 FFT (由于加窗损失了能量，归一化系数为 sum(win))
Y_win = np.fft.fft(y_windowed) / np.sum(win_hanning)

freqs = np.fft.fftfreq(N, 1 / Fs)

# --- 4. 可视化 ---
plt.figure(figsize=(10, 6))

# 子图 1：加窗前后的时域波形比较
plt.subplot(2, 1, 1)
plt.plot(t[:150], y[:150], "b--", alpha=0.6, label="Raw Signal (Rectangular)")
plt.plot(
    t[:150], y_windowed[:150], "r-", linewidth=1.5, label="Windowed (Hanning)"
)
plt.title("Time Domain: Signal with Hanning Window Applied")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# 子图 2：频域对数坐标对比 (dB 刻度更容易看清底噪和拖尾)
plt.subplot(2, 1, 2)
# 转为对数幅值 (dB) 观察泄露拖尾
amp_raw_db = 20 * np.log10(np.abs(Y_raw[: N // 2]) * 2 + 1e-12)
amp_win_db = 20 * np.log10(np.abs(Y_win[: N // 2]) * 2 + 1e-12)

plt.plot(
    freqs[: N // 2], amp_raw_db, "b-", alpha=0.7, label="No Window (High Leakage)"
)
plt.plot(
    freqs[: N // 2],
    amp_win_db,
    "r-",
    linewidth=1.5,
    label="Hanning Window (Suppressed Leakage)",
)

plt.title("Frequency Domain: Spectrum Leakage Comparison (dB scale)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.xlim(30, 70)  # 聚焦 50 Hz 周围
plt.ylim(-80, 5)  # 观察底噪衰减
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()