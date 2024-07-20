import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def remove_baseline(data, sampling_rate):
    nyquist = 0.5 * sampling_rate
    cutoff_freq = 0.1  # 设定基线漂移的截止频率，可以根据实际情况调整
    b, a = signal.butter(4, cutoff_freq, btype='high')
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data

def smooth(data, window_length=5):
    smoothed_data = np.convolve(data, np.ones(window_length)/window_length, mode='same')
    return smoothed_data