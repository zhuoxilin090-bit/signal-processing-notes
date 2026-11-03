import matplotlib.pyplot as plt
import numpy as np

# --- 1. 参数设定 ---
f0 = 2  # 基波频率：2 Hz
T = 1.0  # 观察 1 秒
t = np.linspace(0, T, 1000)

# --- 2. 逐步叠加奇次谐波 ---
harmonics_to_add = [1, 3, 5, 7, 9, 15, 31]  # 要叠加到的最高谐波次数

plt.figure(figsize=(10, 6))

for N in harmonics_to_add:
    # 重新从零开始累加到第 N 次谐波
    y_sum = np.zeros_like(t)
    for n in range(1, N + 1, 2):  # 1, 3, 5, ..., N
        y_sum += (4 / (np.pi * n)) * np.sin(2 * np.pi * (n * f0) * t)

    # 画出当前叠加的结果
    plt.plot(t, y_sum, label=f"Up to {N}th Harmonic")

plt.title("Fourier Synthesis: Building a Square Wave from Sinusoids")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()

#方波的傅里叶级数：第 n 次奇次谐波的幅值是 $4/(n\pi)$，按 $1/n$ 衰减——谐波次数越高，幅值越小。少了 $4/\pi$ 这个系数，叠出来的“方波”幅值只有 $\pi/4 \approx 0.785$，不是 1。