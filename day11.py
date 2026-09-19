import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# --- 1. 参数设置 ---
Fs = 1000  # 采样率 1000 Hz
T = 1.0  # 观察时间 1 秒
t = np.linspace(0, T, int(Fs * T), endpoint=False)

# --- 2. 构造复合非平稳信号 ---
# 成分 A：两个靠的很近的频域信号 (100 Hz 和 120 Hz)
sig_freq = np.sin(2 * np.pi * 100 * t) + np.sin(2 * np.pi * 120 * t)

# 成分 B：在 t = 0.5s 处极短的时域脉冲冲击 (持续 0.02s)
pulse = np.zeros_like(t)
pulse[int(0.49 * Fs) : int(0.51 * Fs)] = 3.0

y = sig_freq + pulse

# --- 3. 分别计算不同 nperseg 参数下的 STFT ---
# Case 1: 小窗口 (高时间分辨率，低频率分辨率)
nperseg_short = 32
f1, t1, Z1 = signal.stft(
    y, fs=Fs, nperseg=nperseg_short, noverlap=nperseg_short - 1
)

# Case 2: 大窗口 (低时间分辨率，高频率分辨率)
nperseg_long = 256
f2, t2, Z2 = signal.stft(
    y, fs=Fs, nperseg=nperseg_long, noverlap=nperseg_long - 1
)

# --- 4. 可视化对比 ---
plt.figure(figsize=(12, 8))

# 原始信号
plt.subplot(3, 1, 1)
plt.plot(t, y, "k-", alpha=0.7)
plt.title(
    "Original Signal: Contains 100Hz & 120Hz + A Sharp Transient Pulse at t=0.5s"
)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# 窄窗口结果 (Small nperseg = 32)
plt.subplot(3, 1, 2)
plt.pcolormesh(t1, f1, np.abs(Z1), shading="gouraud", cmap="magma")
plt.axvline(0.5, color="cyan", linestyle="--", label="True Pulse Time (t=0.5s)")
plt.title(
    "Short Window (nperseg=32): Excellent Time Resolution, Blurred Frequency (100Hz & 120Hz Merged!)"
)
plt.ylabel("Frequency [Hz]")
plt.ylim(0, 200)
plt.legend()

# 宽窗口结果 (Large nperseg = 256)
plt.subplot(3, 1, 3)
plt.pcolormesh(t2, f2, np.abs(Z2), shading="gouraud", cmap="magma")
plt.axvline(0.5, color="cyan", linestyle="--", label="True Pulse Time (t=0.5s)")
plt.title(
    "Long Window (nperseg=256): Excellent Frequency Resolution (100Hz/120Hz Separated!), Smeared Time"
)
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.ylim(0, 200)
plt.legend()

plt.tight_layout()
plt.show()