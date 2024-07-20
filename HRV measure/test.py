import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 示例心率数据（随机生成）
df = pd.read_csv('TIME-HR.csv')
rr_intervals = [30000 / hr for hr in df['HR']]
rr_intervals = np.array(rr_intervals).astype(int)  # 转换为整数类型
concatenated_list = rr_intervals.tolist() * 8
concatenated_array = np.array(concatenated_list)

wd, m = hp.process(rr_intervals, sample_rate=116.99555416894158)

hf = m['hf']
lf = m['lf']
hf_lf_ratio = hf / lf if lf != 0 else float('inf')

print("HF/LF Ratio Analysis:")
print(f"HF: {hf}")
print(f"LF: {lf}")
print(f"HF/LF Ratio: {hf_lf_ratio}")

hp.plotter(wd, m)
plt.show()