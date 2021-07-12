import pandas as pd
import numpy as np
import IPython
from IPython.display import display

data = pd.Series(
        ["Январь", "Февраль","Март","Апрель"],
        index = ["Первый", "Второй", "Третий","Четвертый"]
    )

print(data)

# Доступ к элементам Series
# .loc

print('========')

print(data.loc["Первый"])
print(data.loc[["Первый","Третий"]])

print('========')

print(data['Первый'])
print(data[['Первый','Третий']])

# .iloc

print('=======')

print(data.iloc[0])
print(data.iloc[[0,2]])

print('======')

data = pd.Series(list(range(10,1001)))
print(data.loc[10])
print(data.loc[23])
print(data.loc[245])
print(data.iloc[122])
print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])