# 📈 Signal Processing & Time-Frequency Analysis Learning Notes

本仓库记录了信号处理与时频分析（Time-Frequency Analysis）的学习笔记与 Python 代码实战。

## 📚 目录与学习进度

- **Day 10: 短时傅里叶变换 (STFT) 基础**
  - 使用 `scipy.signal.stft` 计算与绘制二维时频谱图。
  - 理解 `nperseg`（窗口长度）对时频分析的基本影响。
- **Day 11: 海森堡测不准原理与窗口长度权衡**
  - 探究信号处理中的时频分辨率博弈（$\Delta t \cdot \Delta f \ge C$）。
  - 长窗口（高频分、低时分）与短窗口（高时分、低频分）的对比实战。
  - 拓展：小波变换（CWT / PyWavelets）如何通过自适应动态窗口打破固定窗口限制。
- **Day 12: 重叠率 (Overlap) 与 Hop Size 的工程权衡**
  - 理解 `Hop Size` 与 `noverlap` 对时间轴采样密度的影响。
  - 加窗边缘效应补偿与时频谱平滑度分析。
  - 50% ~ 87.5% 重叠率的工程选型与计算量权衡。

## 🛠️ 环境准备

```bash
pip install -r requirements.txt