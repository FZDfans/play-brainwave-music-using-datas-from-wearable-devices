import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def calculate_(freqs, power_spectrum_density):
    """
    计算给定频率范围内的功率谱密度积分。
    
    参数:
    freqs -- 频率数组
    power_spectrum_density -- 功率谱密度数组
    
    返回:
    lf_integral -- 低频范围内的积分值
    hf_integral -- 高频范围内的积分值
    """
    # 定义低频和高频的范围
    lf_range = (0.04, 0.15)  # 低频范围：0.04 Hz 到 0.15 Hz
    hf_range = (0.15, 0.4)   # 高频范围：0.15 Hz 到 0.4 Hz

    # 查找落在指定频率范围内的索引
    idx_lf = np.where((freqs >= lf_range[0]) & (freqs <= lf_range[1]))[0]
    idx_hf = np.where((freqs >= hf_range[0]) & (freqs <= hf_range[1]))[0]

    # 对指定频率范围内的功率谱密度进行积分
    lf_integral = np.trapz(power_spectrum_density[idx_lf], freqs[idx_lf])  # 低频积分
    hf_integral = np.trapz(power_spectrum_density[idx_hf], freqs[idx_hf])  # 高频积分
    result = hf_integral/lf_integral
    print(hf_integral)
    print('\n')
    print(lf_integral)
    return result
def HRana(arr):
    sampling_rate = 50
    num_samples = len(arr)

    # 进行快速傅立叶变换
    fft_result = np.fft.fft(arr)
    # 计算频率轴
    freqs = np.fft.fftfreq(num_samples, d=1/sampling_rate)
    # 计算功率谱密度
    power_spectrum_density = np.abs(fft_result)**2 / num_samples

    # 仅保留正频率部分（因为FFT结果是对称的）
    positive_freq_mask = freqs > 0
    freqs = freqs[positive_freq_mask]
    power_spectrum_density = power_spectrum_density[positive_freq_mask]
    return calculate_(freqs,power_spectrum_density)

from scipy import signal

def remove_baseline(data, sampling_rate):
    nyquist = 0.5 * sampling_rate
    cutoff_freq = 0.02  # 设定基线漂移的截止频率，可以根据实际情况调整
    b, a = signal.butter(4, 0.04, btype='high')
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data

def smooth(data, window_length=5):
    smoothed_data = np.convolve(data, np.ones(window_length)/window_length, mode='same')
    return smoothed_data
df = pd.read_csv('yd.csv')
df = df['HR']
df = np.array(df)
df = remove_baseline(smooth(df),50)
HF_LF_rate=HRana(df)
