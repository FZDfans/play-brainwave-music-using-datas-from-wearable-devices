import pandas as pd

# 读取原始 CSV 文件
df = pd.read_csv('output.csv')

# 提取特定的列，例如"time"和"HR"
selected_data = df[['Time', 'Ax','Ay','Az']]

# 将选定的数据保存为新的 CSV 文件
selected_data.to_csv('TIME-accel.csv', index=False)

print("已经成功提取并保存所需的数据到 TIME-accel.csv 文件中。")