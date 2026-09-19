import matplotlib.pyplot as plt
import numpy as np

# --- 1. 生成一个标准方波（周期 T = 1s, 频率 f0 = 1Hz）---
f0 = 1.0
T = 1.0
t = np.linspace(0, T, 1000)

# 用 np.sign 快速生成一个 1Hz 的标准方波 (幅值为 -1 到 1)
y_square = np.sign(np.sin(2 * np.pi * f0 * t))

# --- 2. 手动用“正交性”求取各个谐波的系数 (b_n) ---
harmonics = range(1, 9)  # 检测 1 到 8 次谐波
b_n_calculated = []

for n in harmonics:
    # 将原信号与频率为 n*f0 的正弦波相乘，并在一个周期内积分（求均值后乘2）
    detector_wave = np.sin(2 * np.pi * (n * f0) * t)
    # 离散积分：(2/T) * sum(y * detector) * dt
    b_n = (2 / len(t)) * np.sum(y_square * detector_wave)
    b_n_calculated.append(b_n)

# --- 3. 可视化计算出的谐波系数 ---
plt.figure(figsize=(9, 4))
plt.bar(harmonics, b_n_calculated, color="teal", alpha=0.7)

# 标出理论值 (对于幅值为1的方波，奇次谐波理论幅值为 4/(n*pi))
for n in range(1, 9, 2):
    theoretical_val = 4 / (n * np.pi)
    plt.plot(
        n,
        theoretical_val,
        "ro",
        label="Theoretical Value (4/nπ)" if n == 1 else "",
    )

plt.title("Calculated Fourier Coefficients (b_n) for Square Wave")
plt.xlabel("Harmonic Order (n)")
plt.ylabel("Calculated Amplitude")
plt.grid(True, axis="y")
plt.legend()
plt.tight_layout()
plt.show()

# 打印具体数值
for n, val in zip(harmonics, b_n_calculated):
    print(f"{n}次谐波计算幅值: {val:.4f}")