import matplotlib.pyplot as plt
import numpy as np

# --- 1. 参数设定 ---
f = 5  # 信号频率：5 Hz（每秒震动 5 次）
T = 1.0  # 观察时间：1 秒

# --- 2. 模拟“连续信号”（用非常密集的采样点来近似）---
t_continuous = np.linspace(0, T, 1000)  # 1秒内取 1000 个点，看起来就像一条光滑的曲线
y_continuous = np.sin(2 * np.pi * f * t_continuous)

# --- 3. 离散采样（以 Fs = 20 Hz 进行采样）---
Fs = 20  # 采样频率：每秒采 20 个点
t_sampled = np.arange(0, T, 1 / Fs)  # 采样时间点
y_sampled = np.sin(2 * np.pi * f * t_sampled)

# --- 4. 可视化对比 ---
plt.figure(figsize=(10, 4))

# 画出理论上的连续波形（蓝色实线）
plt.plot(
    t_continuous,
    y_continuous,
    label="Continuous Signal (Analog)",
    color="blue",
    alpha=0.5,
)

# 画出电脑实际保存的采样点（红色离散点与柱状茎图）
plt.stem(
    t_sampled,
    y_sampled,
    linefmt="r-",
    markerfmt="ro",
    basefmt="k-",
    label=f"Sampled Points (Fs = {Fs} Hz)",
)

plt.title(f"Sinusoidal Signal (f = {f} Hz) vs. Discrete Sampling")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 2 * np.pi * f * t：这就是角频率公式 $\omega t = 2\pi f t$ 在 Python 中的表达。
# np.arange(0, T, 1 / Fs)：在 NumPy 中，生成步长为 $\Delta t = 1/F_s$ 的时间序列，直接对应电脑采样的时间节点。
# plt.stem(...)：这是信号处理中专门用来绘制离散序列（Stem Plot / 茎图）的函数，也是你以后在信号处理教材里最常看到的画法。