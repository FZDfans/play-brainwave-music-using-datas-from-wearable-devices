import pandas as pd
import matplotlib.pyplot as plt

# 读取包含时间和心率数据的 CSV 文件
df = pd.read_csv('TIME-HR.csv')

# 计算心率变化率
time_interval = 0.02
df['HR_change_rate'] = df['HR'].diff() / time_interval

# 可视化心率和变化率
plt.figure(figsize=(12, 6))

# 绘制心率
plt.subplot(2, 1, 1)
plt.plot(df['Time'], df['HR'], color='blue', label='Heart Rate (HR)', linewidth=2)
plt.title('Heart Rate Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Heart Rate (bpm)')
plt.legend()
plt.grid()

# 绘制心率变化率
plt.subplot(2, 1, 2)
plt.plot(df['Time'], df['HR_change_rate'], color='red', label='HR Change Rate', linewidth=2)
plt.title('Heart Rate Change Rate Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Change Rate (bpm/s)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()