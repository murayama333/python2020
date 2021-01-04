import numpy as np

# 小数点以下の桁数を3桁に設定
np.set_printoptions(precision=3, floatmode='fixed')

array = np.random.rand(5, 5)

print(array)
