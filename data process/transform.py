import csv

# 时间间隔和初始时间
time_interval = 0.02
initial_time = 0

# 输入的数据文件和输出的CSV文件
input_file = 'fix-yd-data.dat'
output_csv = 'yd.csv'

# 打开输入的数据文件和输出的CSV文件
with open(input_file, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
    # CSV写入器，用逗号作为分隔符
    csv_writer = csv.writer(outfile, delimiter=',')

    # 写入CSV的表头，根据实际情况调整
    csv_writer.writerow(['Time', 'GRS', 'Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz', 'HR', 'SPO2'])

    # 初始化时间
    current_time = initial_time

    # 逐行读取.dat文件中的数据
    for line in infile:
        # 去除行尾换行符并按逗号分割数据
        parts = line.strip().split(',')

        # 初始化一个空列表，用于存储处理后的数据行
        data_row = [f"{current_time:.2f}"]

        # 遍历每个部分，将键值对拆分并加入到data_row中
        for part in parts:
            key_value = part.split(':')
            key = key_value[0].strip()
            value = key_value[1].strip()
            data_row.append(value)

        # 将处理后的一行数据写入CSV文件
        csv_writer.writerow(data_row)

        # 更新时间
        current_time += time_interval

print(f"数据已经从 {input_file} 转换并保存到 {output_csv} 中。")