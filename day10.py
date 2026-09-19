import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# --- 1. 参数设定 ---
Fs = 1000  # 采样率 1000 Hz
T = 2.0  # 总时长 2 秒
t = np.linspace(0, T, int(Fs * T), endpoint=False)

# --- 2. 构造非平稳信号：Chirp 信号 (频率从 10 Hz 线性增加到 300 Hz) ---
# 使用 scipy.signal.chirp 自动生成扫频信号
y = signal.chirp(t, f0=10, t1=T, f1=300, method="linear")

# --- 3. 核心步骤：计算 STFT ---
# nperseg: 每个窗口的长度 (采样点数)
# noverlap: 窗口重叠的采样点数 (通常设为 nperseg 的 50% - 75%)
nperseg = 128
noverlap = 96

f_stft, t_stft, Zxx = signal.stft(
    y, fs=Fs, window="hann", nperseg=nperseg, noverlap=noverlap
)

# Zxx 是一个二维复数矩阵：行代表【频率】，列代表【时间】
# 取模计算幅值谱
amplitude_stft = np.abs(Zxx)

# --- 4. 可视化：1D 传统 FFT vs 2D STFT 时频谱图 ---
plt.figure(figsize=(10, 8))

# 子图 1：1D 时域波形 (能看出频率越来越密，但读不出精准数值)
plt.subplot(3, 1, 1)
plt.plot(t, y, "b-", alpha=0.7)
plt.title("1. Time Domain: Chirp Signal (10 Hz -> 300 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# 子图 2：传统 1D FFT 频谱 (只能看到 10-300Hz 间有一片能量，丢失了时间信息)
Y_fft = np.fft.fft(y) / len(y)
freqs_fft = np.fft.fftfreq(len(y), 1 / Fs)
plt.subplot(3, 1, 2)
plt.plot(freqs_fft[: len(y) // 2], np.abs(Y_fft[: len(y) // 2]) * 2, "r-")
plt.title(
    "2. Traditional FFT: Lost Time Information (Just a flat broad band)"
)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0, 400)
plt.grid(True)

# 子图 3：2D STFT 时频谱图 (Spectrogram) - 完美呈现【频率随时间的演变】！
plt.subplot(3, 1, 3)
# pcolormesh 用于绘制二维热力图，cmap='jet' 或 'viridis'
plt.pcolormesh(
    t_stft, f_stft, amplitude_stft, shading="gouraud", cmap="viridis"
)
plt.title("3. STFT Spectrogram: Clear Time-Frequency Evolution!")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.ylim(0, 400)
plt.colorbar(label="Magnitude")

plt.tight_layout()
plt.show()