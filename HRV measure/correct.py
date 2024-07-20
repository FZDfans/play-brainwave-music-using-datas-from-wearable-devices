# 指定原始数据文件和目标文件
input_file = 'dat.dat'
output_file = 'fixed_data.dat'

# 打开原始数据文件和目标文件
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # 逐行读取原始数据文件
    for line in infile:
        # 替换每行中的"."为","
        fixed_line = line.replace('.', ',')

        # 将修正后的行写入目标文件
        outfile.write(fixed_line)

print(f"数据已经从 {input_file} 处理并保存到 {output_file} 中。")
