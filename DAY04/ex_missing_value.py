# 결측치 체크 및 검사
# DataFrame.isnull() / isna() -> True/False => 원소마다 검사
import pandas as pd
import numpy as np
import sys
sys.path.append(R'C:\Users\KDT38\Desktop\KDT_14\[2]PANDAS\utils')
import utils as u

## DF 생성
print("--------------------------------------------------------------")
df = pd.DataFrame(
    dict( 
        age = [ 5, 6, np.nan ],
        born = [ pd.NaT, pd.Timestamp('1939-05-27'),
        pd.Timestamp('1940-04-25')],
        name = ['Alfred', 'Batman', ''],
        toy = [None, 'Batmobile', 'Joker']
    )
)
## DF 출력
print( df )
print("--------------------------------------------------------------")

u.data_info(df)
print()


print("--------------------------------------------------------------")
# 결측치 체크
print(f"결측치 체크 isna() >>>\n{df.isna()}")
print(f"\n결측치 체크 isnull() >>>\n{df.isnull()}")
