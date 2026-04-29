# 중복 데이터 검사 및 처리
# 검사: DataFrame.duplicated() True/False
# 처리: DataFrame.drop_duplicates()

import pandas as pd
import numpy as np
import sys
sys.path.append(R'C:\Users\KDT38\Desktop\KDT_14\[2]PANDAS\utils')
import utils as u

## DF 생성
print("--------------------------------------------------------------")
df = pd.DataFrame(  
    { 
        'brand' : [ 'Yum', 'Yum', 'Indo', 'Indo', 'Indo' ],
        'style' : [ 'cup', 'cup', 'cup', 'pack', 'pack' ],
        'rating' : [4, 4, 3.5, 15, 5]
    }
)

## DF 출력
print( df )
print("--------------------------------------------------------------")

u.data_info(df)
print()


print("--------------------------------------------------------------")
# 행 단위로 중복여부 검사 후 True/False 반환
print(df, '\n')
print(f"중복 데이터 검사 -> duplicated() >>>\n{df.duplicated()}")
print()
print(f"중복 개수 확인 >>>\n{df.duplicated().sum()}")
print("--------------------------------------------------------------")
print()


print("--------------------------------------------------------------")
# 중복 데이터 처리
print(df, '\n')
print(f"중복 데이터 처리 -> drop_duplicates() >>>\n{df.drop_duplicates()}")
print("--------------------------------------------------------------")
print()



print("--------------------------------------------------------------")
# 중복 데이터 처리
print(df, '\n')
print(f"중복 데이터 처리 -> drop_duplicates() >>>\n{df.drop_duplicates(subset='brand')}")
print("--------------------------------------------------------------")
print()


