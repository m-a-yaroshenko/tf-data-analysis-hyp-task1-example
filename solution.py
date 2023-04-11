import pandas as pd
import numpy as np
import math


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p_c = x_success / x_cnt
    p_t = y_success / y_cnt
    SE = math.sqrt((p_t*(1-p_t))/y_cnt + (p_c*(1-p_c))/x_cnt)
    z_stat = (p_t - p_c) / SE
    z_crit = 1.645 # при alpha=0.09
    return True if abs(z_stat) > z_crit else False
