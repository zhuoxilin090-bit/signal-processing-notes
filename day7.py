import matplotlib.pyplot as plt
import numpy as np

# --- 1. 参数设置 ---
Fs = 1000  # 采样率 1000 Hz
f1, f2 = 50, 52  # 两个非常接近的频率 (相差仅 2 Hz)

# --- 实验 1：采集时间过短 (T = 0.25s, N = 250 点, Δf = 4 Hz) ---
t1 = np.arange(0, 0.25, 1 / Fs)
y1 = np.sin(2 * np.pi * f1 * t1) + np.sin(2 * np.pi * f2 * t1)

Y1_fft = np.fft.fft(y1) / len(y1)
freqs1 = np.fft.fftfreq(len(y1), 1 / Fs)

# --- 实验 2：短信号 + 零填充 (Zero-Padding 到 2000 点) ---
N_pad = 2000
Y2_fft = np.fft.fft(y1, n=N_pad) / len(y1)  # 指定 n 参数自动补零
freqs2 = np.fft.fftfreq(N_pad, 1 / Fs)

# --- 实验 3：增加真实采集时间 (T = 2.0s, N = 2000 点, Δf = 0.5 Hz) ---
t3 = np.arange(0, 2.0, 1 / Fs)
y3 = np.sin(2 * np.pi * f1 * t3) + np.sin(2 * np.pi * f2 * t3)

Y3_fft = np.fft.fft(y3) / len(y3)
freqs3 = np.fft.fftfreq(len(y3), 1 / Fs)

# --- 2. 可视化对比 ---
plt.figure(figsize=(10, 7))

# 画图 1：短采样时间 (分辨不清，混成一个大包)
plt.subplot(3, 1, 1)
plt.plot(freqs1[:100], np.abs(Y1_fft[:100]) * 2, "ro-", label="T = 0.25s (Δf = 4 Hz)")
plt.title("Case 1: Short Duration - Cannot Resolve 50 Hz and 52 Hz")
plt.xlim(40, 60)
plt.grid(True)
plt.legend()

# 画图 2：短采样时间 + 补零 Zero-Padding (曲线变平滑，但依然无法分离)
plt.subplot(3, 2, 3)
plt.plot(
    freqs2[:200],
    np.abs(Y2_fft[:200]) * 2,
    "b-",
    label="T = 0.25s + Zero Padding (n=2000)",
)
plt.title("Case 2: Zero-Padding (Smooth curve, but NO extra resolution)")
plt.xlim(40, 60)
plt.grid(True)
plt.legend()

# 画图 3：真实长采样时间 (清晰地分离开两个独立的尖峰)
plt.subplot(3, 1, 3)
plt.plot(
    freqs3[:200],
    np.abs(Y3_fft[:200]) * 2,
    "g-",
    linewidth=1.5,
    label="T = 2.0s (Δf = 0.5 Hz)",
)
plt.title("Case 3: Long Duration - Clearly Resolved Two Peaks!")
plt.xlim(40, 60)
plt.xlabel("Frequency [Hz]")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()