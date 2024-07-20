import time
import pandas as pd
import numpy as np
from HBR import HBR
from HR import HRana
from sig import savesignals
from HRprocess import remove_baseline, smooth
from send_speakers import send_data
while True:
    # 5秒内生成模拟信号并在每个0.02秒周期处理信号
    start_time = time.time()
    while time.time() - start_time < 5:
        savesignals()
        time.sleep(0.02)
    print("数据存储完成！")
    
    # 处理数据和特征提取, 然后分析这个人的行为
    df = pd.read_csv('abc.csv')
    df = df[['Ax','Ay','Az']]
    pre = HBR(df)
    
    # 处理 pre DataFrame
    pre = pre.replace([1, 2, 4, 5, 6, 7], 0)
    pre = pre.replace([3, 13, 14, 130, 140], 1)
    pre = pre.replace(8, 2)
    
    # 使用 HR 进行交感神经和副交感神经的活动评价
    df2 = pd.read_csv('abc.csv')
    df2 = df2[['HR']]
    df_arr = df2.to_numpy().flatten()
    arr = np.array(df_arr)
    arr = remove_baseline(arr, 50)
    arr = smooth(arr)
    rate = HRana(arr)
    
    if rate <= 1.5:
        HH = 0
    else:
        HH = 1
    
    # 进行最基础的心率评价
    dataframe = pd.read_csv('abc.csv')
    greater_count = dataframe['HR'].gt(100).sum()
    total_count = len(dataframe['HR'])
    proportion = greater_count / total_count

    X = None
    
    # 根据条件决定 X 的值
    if proportion > 0.05:
        X = 0
    elif HH == 0:
        X = 1
    elif proportion <= 0.05 and HH == 1:
        # 取 pre DataFrame 的最后 500 个元素
        last_500 = pre.tail(500)
        # 统计每个值的出现次数
        counts = last_500['label'].value_counts()
        # 确定出现次数最多的值
        most_frequent_value = counts.idxmax()
        if most_frequent_value == 0:
            X = 2
        elif most_frequent_value == 1:
            X = 1
        elif most_frequent_value == 2:
            X = 3
    
    print(f'决定播放音乐的模式: {X}')
    #send_data(speaker_address,X) 这是向蓝牙音箱发送经过模型处理的变量的函数，还要你去填音箱的地址
    time.sleep(10)


