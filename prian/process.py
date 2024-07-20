import pandas as pd

# 读取原始 CSV 文件
df = pd.read_csv('D:\科研\ICAN挑战杯\scripts\prian\harth\S006.csv')

# 提取特定的列，例如"time"和"HR"
selected_data = df[['timestamp', 'back_x','back_y','back_z','label']]

# 将选定的数据保存为新的 CSV 文件
selected_data.to_csv('D:\科研\ICAN挑战杯\scripts\prian\processed-data\S006_.csv', index=False)

print("已经成功提取并保存所需的数据到文件中。")