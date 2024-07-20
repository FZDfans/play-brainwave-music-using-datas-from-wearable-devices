import random
import pandas as pd
import re
from extraction import processing
from save import save_to_csv
from HBR import HBR
from musicplay import play_music


def savesignals():
    # 生成模拟数据
    gsr = random.randint(990, 1006)
    ax = random.randint(-3500, -3300)
    ay = random.randint(-500, 0)
    az = random.randint(20000, 20600)
    gx = random.randint(380, 480)
    gy = random.randint(-480, -380)
    gz = random.randint(30, 80)
    hr = random.randint(74, 75)
    spo2 = 59

    # 格式化成字符串
    data_RAW = f"GSR:{gsr},Ax:{ax},Ay:{ay},Az:{az},Gx:{gx},Gy:{gy},Gz:{gz}.HR:{hr},SPO2:{spo2}"
    data_corrected = data_RAW.replace('.', ',')
    data_corrected = re.sub(r'^\\W+|\\W+$', '', data_corrected)
    save_to_csv(data_corrected,'abc.csv',0.02)