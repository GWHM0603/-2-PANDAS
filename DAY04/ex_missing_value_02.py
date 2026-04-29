# 결측치 처리 - 삭제

# DataFrame.dropna() 기본: 행 단위. 1개라도 결측치 있으면 삭제
# axis = 0        삭제 축 기준
# how = 'any'     삭제 방법
# thresh = 숫자    정상 데이터의 최소 개수 설정
# subset = 컬럼명  특정 컬럼만 결측치 검사

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
# 결측치 삭제: dropna()
print(df, '\n')
print(f"행 단위 삭제 dropna() >>>\n{df.dropna()}")
print("--------------------------------------------------------------")
print()

print("--------------------------------------------------------------")
# 결측치 삭제: dropna()
print(df, '\n')
print(f"모든 데이터가 결측치면 삭제  dropna(how = 'all') >>>\n{df.dropna(how = 'all')}")
print("--------------------------------------------------------------")

print("--------------------------------------------------------------")
# 결측치 삭제: dropna()
print(df, '\n')
print(f"열 단위 삭제 dropna(axis = 1) >>>\n{df.dropna(axis = 1)}")
print("--------------------------------------------------------------")


print("--------------------------------------------------------------")
# 결측치 삭제: dropna()
print(df, '\n')
print(f"모든 데이터가 결측치일 때, 열 단위 삭제 dropna(axis = 1, how = 'all') >>>\n{df.dropna(axis = 1, how = 'all')}")
print("--------------------------------------------------------------")


print("--------------------------------------------------------------")
# 결측치 삭제: dropna()
print(df, '\n')
print(f"컬럼 방향 기준 + 생년월일 결측치인 행 삭제) >>>\n{df.dropna(subset=['born'])}")
print("--------------------------------------------------------------")