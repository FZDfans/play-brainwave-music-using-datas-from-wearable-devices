import pandas as pd
import os

# 设置原始数据集文件夹路径和输出文件夹路径
input_folder = 'D:\科研\ICAN挑战杯\scripts\prian\harth'  # 替换成你的输入文件夹路径
output_folder = 'D:\科研\ICAN挑战杯\scripts\prian\processed-data'  # 替换成你的输出文件夹路径

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取文件夹内所有以 .csv 结尾的文件列表
file_list = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# 遍历处理每个文件
for file in file_list:
    file_path = os.path.join(input_folder, file)
    # 读取原始数据集
    df = pd.read_csv(file_path)

    # 提取指定列
    df_processed = df[['timestamp', 'back_x', 'back_y', 'back_z', 'label']].copy()

    # 将 'timestamp' 列转换为秒级别
    df_processed['timestamp'] = pd.to_datetime(df_processed['timestamp']).dt.time.apply(lambda x: (x.hour * 3600 + x.minute * 60 + x.second + x.microsecond / 1_000_000))
    df_processed['timestamp'] = df_processed['timestamp'].round(2)
    # 将 'back_x', 'back_y', 'back_z' 列的值乘以10000
    df_processed['back_x'] *= 10000
    df_processed['back_y'] *= 10000
    df_processed['back_z'] *= 10000

    # 重命名列
    df_processed.rename(columns={
        'timestamp': 'Time',
        'back_x': 'Ax',
        'back_y': 'Ay',
        'back_z': 'Az'
    }, inplace=True)

    # 构造输出文件路径
    output_file = os.path.join(output_folder, f'processed_{file}')

    # 保存处理后的数据为新的CSV文件
    df_processed.to_csv(output_file, index=False)

    print(f"已处理文件 {file} 并保存为 {output_file}")

print("批量处理完成！")