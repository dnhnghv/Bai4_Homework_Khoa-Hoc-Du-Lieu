import pandas as pd
df = pd.DataFrame({
    'Ten':[6,2,1],
    'A':[4,5,6],
    'B':[7,8,9]
})
print (df ==8)
print (df [df==8])
print (df [df['B']==8])
