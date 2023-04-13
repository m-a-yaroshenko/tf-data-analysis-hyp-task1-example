import pandas as pd
import numpy as np
import scipy.stats as stats


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    conv_control = x_success / x_cnt
    conv_test = y_success / y_cnt
    diff = conv_test - conv_control
    se = ((1-conv_test)/y_cnt + (1-conv_control)/x_cnt)**0.5
    t_stat = diff/se
    p_value = 2*(1 - stats.t.cdf(abs(t_stat), x_cnt + y_cnt - 2))
    alpha = 0.09
    return True if p_value <= alpha else False
