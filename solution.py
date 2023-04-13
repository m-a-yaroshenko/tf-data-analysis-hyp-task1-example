import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import norm


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной


def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    SE = ((p1*(1-p1))/x_cnt + (p2*(1-p2))/y_cnt) ** 0.5
    Z = (p2 - p1) / SE
    Z_alpha = norm.ppf(1 - 0.09/2)
    return True if Z > Z_alpha else False
  
