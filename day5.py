import matplotlib.pyplot as plt
import numpy as np

# --- 1. 参数设置 ---
f0 = 1.0  # 基波 1 Hz
T = 1.0
t = np.linspace(-T / 2, T / 2, 1000)  # 时间轴关于 0 对称：[-0.5s, 0.5s]

# --- 2. 构造奇方波与偶方波 ---
y_odd = np.sign(np.sin(2 * np.pi * f0 * t))  # 奇函数：sin 形式
y_even = np.sign(np.cos(2 * np.pi * f0 * t))  # 偶函数：cos 形式

# --- 3. 计算前 5 次谐波的 sin(b_n) 与 cos(a_n) 分量 ---
harmonics = range(1, 6)
odd_sin_coeffs, odd_cos_coeffs = [], []
even_sin_coeffs, even_cos_coeffs = [], []

for n in harmonics:
    sin_wave = np.sin(2 * np.pi * n * f0 * t)
    cos_wave = np.cos(2 * np.pi * n * f0 * t)

    # 奇信号系数提取
    odd_sin_coeffs.append(
        (2 / len(t)) * np.sum(y_odd * sin_wave)
    )  # sin 分量 (b_n)
    odd_cos_coeffs.append(
        (2 / len(t)) * np.sum(y_odd * cos_wave)
    )  # cos 分量 (a_n)

    # 偶信号系数提取
    even_sin_coeffs.append(
        (2 / len(t)) * np.sum(y_even * sin_wave)
    )  # sin 分量 (b_n)
    even_cos_coeffs.append(
        (2 / len(t)) * np.sum(y_even * cos_wave)
    )  # cos 分量 (a_n)

# --- 4. 可视化对比 ---
fig, axes = plt.subplots(2, 2, figsize=(11, 6))

# 第一排：奇函数及其分解
axes[0, 0].plot(t, y_odd, "g", label="Odd Square Wave")
axes[0, 0].set_title("Odd Signal f(-t) = -f(t)")
axes[0, 0].grid(True)

x_bars = np.arange(len(harmonics))
axes[0, 1].bar(
    x_bars - 0.15, odd_sin_coeffs, width=0.3, label="sin (b_n)", color="blue"
)
axes[0, 1].bar(
    x_bars + 0.15, odd_cos_coeffs, width=0.3, label="cos (a_n)", color="orange"
)
axes[0, 1].set_title("Energy Spectrum: ONLY sin terms exist!")
axes[0, 1].set_xticks(x_bars)
axes[0, 1].set_xticklabels(harmonics)
axes[0, 1].grid(True)
axes[0, 1].legend()

# 第二排：偶函数及其分解
axes[1, 0].plot(t, y_even, "r", label="Even Square Wave")
axes[1, 0].set_title("Even Signal f(-t) = f(t)")
axes[1, 0].grid(True)

axes[1, 1].bar(
    x_bars - 0.15, even_sin_coeffs, width=0.3, label="sin (b_n)", color="blue"
)
axes[1, 1].bar(
    x_bars + 0.15, even_cos_coeffs, width=0.3, label="cos (a_n)", color="orange"
)
axes[1, 1].set_title("Energy Spectrum: ONLY cos terms exist!")
axes[1, 1].set_xticks(x_bars)
axes[1, 1].set_xticklabels(harmonics)
axes[1, 1].grid(True)
axes[1, 1].legend()

plt.tight_layout()
plt.show()