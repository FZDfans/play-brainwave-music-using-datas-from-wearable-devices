import csv

# 全局计数器，初始为0
global_counter = 0

def save_to_csv(data_string, output_file, interval):
    global global_counter
    
    # 如果是每个周期的开始，清空文件
    if global_counter == 0:
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(['Time', 'GSR', 'Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz', 'HR', 'SPO2'])
    
    # 打开CSV文件，使用 'a' 模式追加内容，newline='' 用于处理换行符
    with open(output_file, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        
        # 计算当前时间点
        current_time = global_counter * interval
        
        # 将 data_string 按逗号分割成键值对列表
        key_value_pairs = data_string.split(',')
        
        data_row = [current_time]
        
        # 遍历每个部分，将键值对拆分并加入到 data_row 中
        for part in key_value_pairs:
            key_value = part.split(':')
            key = key_value[0].strip()
            value = key_value[1].strip()
            data_row.append(value)
        
        # 写入CSV文件的一行数据
        csv_writer.writerow(data_row)
    
    # 更新全局计数器
    global_counter += 1