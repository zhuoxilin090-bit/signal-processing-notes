import matplotlib.pyplot as plt
import numpy as np

# --- 1. 参数设定 ---
f_high = 9  # 真实高频信号：9 Hz
Fs = 10  # 采样频率：10 Hz（低于 2 * 9 = 18 Hz，触发混叠！）
T = 1.0  # 观察时间 1 秒

# 理论预测的“伪装低频信号”频率：|f - Fs| = |9 - 10| = 1 Hz
f_alias = abs(f_high - Fs)

# --- 2. 模拟连续信号与采样 ---
t_continuous = np.linspace(0, T, 1000)
y_high_continuous = np.sin(2 * np.pi * f_high * t_continuous)  # 真实的 9Hz 信号

t_sampled = np.arange(0, T, 1 / Fs)
y_sampled = np.sin(2 * np.pi * f_high * t_sampled)  # 采样得到的点

y_alias_continuous = np.sin(
    2 * np.pi * f_alias * t_continuous
)  # 预测的 1Hz 假信号

# --- 3. 可视化 ---
plt.figure(figsize=(10, 5))

# 画出真实的 9Hz 高频信号（灰色虚线）
plt.plot(
    t_continuous,
    y_high_continuous,
    "--",
    color="gray",
    alpha=0.5,
    label="Original Real Signal (9 Hz)",
)

# 画出混叠出来的 1Hz 假信号（红色虚线）
plt.plot(
    t_continuous,
    -y_alias_continuous,
    ":",
    color="red",
    linewidth=2,
    label=f"Aliased Signal ({f_alias} Hz)",
)

# 画出实际采样点（蓝色点）
plt.stem(
    t_sampled,
    y_sampled,
    linefmt="b-",
    markerfmt="bo",
    basefmt="k-",
    label=f"Sampled Points (Fs = {Fs} Hz)",
)

plt.title(
    f"Aliasing Experiment: 9 Hz Signal Sampled at 10 Hz Appears as {f_alias} Hz!"
)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()