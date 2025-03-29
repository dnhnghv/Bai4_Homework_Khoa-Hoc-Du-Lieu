import pandas as pd
import numpy as np
df = pd.DataFrame({
    'A' : [1, np.nan,3,4],
    'B' : [ np.nan,2 ,3,np.nan]
})

df_sau_dien = df.fillna(df.mean())
print(df_sau_dien)