import matplotlib.pyplot as plt
import numpy as np

# --- 1. 构造真实信号与高频噪声 ---
Fs = 1000  # 采样率 1000 Hz
T = 1.0  # 观察时间 1 秒
N = int(Fs * T)
t = np.linspace(0, T, N, endpoint=False)

# 有用信号：10 Hz 的低频正弦波 (例如机械转速信号)
clean_signal = np.sin(2 * np.pi * 10 * t)

# 高频噪声：200 Hz 的干扰信号 + 随机高斯白噪声
noise = 0.6 * np.sin(2 * np.pi * 200 * t) + np.random.normal(0, 0.3, N)

# 最终叠加的带噪信号 (在时域上看起来一片混乱)
noisy_signal = clean_signal + noise

# --- 2. 步骤一：FFT 变换 ---
Y_fft = np.fft.fft(noisy_signal)
freqs = np.fft.fftfreq(N, 1 / Fs)

# --- 3. 步骤二：设计频域低通滤波器 (Low-pass Filter Mask) ---
cutoff_freq = 30  # 截止频率设为 30 Hz (高于 10 Hz，低于 200 Hz)

# 创建掩码：频率绝对值小于 30 Hz 的保留(1)，其余清零(0)
# 注意：FFT 是对称的，np.abs(freqs) 可以同时处理正负频率！
filter_mask = np.abs(freqs) < cutoff_freq

# 应用滤波器：将高频部分的频域系数置零
Y_filtered = Y_fft * filter_mask

# --- 4. 步骤三：iFFT 逆变换重构时域信号 ---
# np.fft.ifft 还原回复数，取 np.real 得到真实时域波形
reconstructed_signal = np.real(np.fft.ifft(Y_filtered))

# --- 5. 可视化对比 ---
plt.figure(figsize=(10, 8))

# 图 1：时域信号对比 (原始干净 vs 带噪 vs 重构)
plt.subplot(3, 1, 1)
plt.plot(t, noisy_signal, "gray", alpha=0.5, label="Noisy Signal")
plt.plot(t, clean_signal, "g--", linewidth=2, label="Original Clean (10 Hz)")
plt.plot(
    t,
    reconstructed_signal,
    "r-",
    linewidth=1.5,
    label="Filtered Signal (Reconstructed)",
)
plt.title("Time Domain: Signal Reconstruction via iFFT")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc="upper right")

# 图 2：滤波前的频谱
plt.subplot(3, 1, 2)
plt.plot(
    freqs[: N // 2],
    np.abs(Y_fft[: N // 2]) / N * 2,
    "b-",
    label="Raw Spectrum (Signal + Noise)",
)
plt.axvline(
    cutoff_freq, color="k", linestyle="--", label=f"Cutoff ({cutoff_freq} Hz)"
)
plt.title("Frequency Domain: Before Filtering")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0, 300)
plt.grid(True)
plt.legend()

# 图 3：滤波后的频谱
plt.subplot(3, 1, 3)
plt.plot(
    freqs[: N // 2],
    np.abs(Y_filtered[: N // 2]) / N * 2,
    "r-",
    label="Filtered Spectrum (High Freq Cleared)",
)
plt.title("Frequency Domain: After Filtering (High Frequencies Zeroed)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0, 300)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()