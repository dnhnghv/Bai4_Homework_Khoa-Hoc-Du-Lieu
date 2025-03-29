import numpy as np
import pandas as pd
df = pd.DataFrame({
    'Tháng': ['Jan', 'Jan', 'Feb', 'Feb'],
    'Nhóm': ['A', 'B', 'A', 'B'],
    'Doanh thu': [100, 150, 200, 250]
})

df_pivot = df.pivot_table(values='Doanh thu', index='Tháng', columns='Nhóm', aggfunc='sum')
print(df_pivot)


df = pd.DataFrame({
    'Nhóm': ['A', 'A', 'B', 'B', 'C'],
    'Doanh thu': [10, 15, 20, 25, 30]
})

df_grouped = df.groupby('Nhóm').sum()  # Tính tổng doanh thu theo nhóm
print(df_grouped)