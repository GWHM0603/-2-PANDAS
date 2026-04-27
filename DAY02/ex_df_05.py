## ===========================================
##          DataFrame 행과 열 다루기
## -------------------------------------------
## 여러 행 선택 - [1] 인덱스 리스트
## >>> df변수명.iloc[[정수 위치인덱스, ..., n]]
## >>> df변수명.loc[[라벨 인덱스, ..., n]]
## 여러 열 선택
## >>> df변수명[[컬럼 이름, ..., n]]
## ===========================================

import pandas as pd 

datas = [ [11,33,55,77], 
            [ 2,22, 4,44] , 
            ['A',10,'B',0] ]

df = pd.DataFrame(datas, index = ['1st', '2nd', '3rd'], columns = ['A', 'B', 'C', 'D'])

print('[&&] DataFrame 기본 속성들\n')
print(f'[1] index: {df.index}\n')  
print(f'[2] columns: {df.columns}\n')  

# 여러 열/컬럼 선택하기 1 - df[[컬럼 이름, ...]]
# 컬럼 이름 지정시 위치 인덱스 지원 x
print('==== 컬럼 선택 ====\n')
print("A, B, C 컬럼 선택하기: ", type(df[['A', 'B', 'C']]))
print(df[['A', 'B', 'C']])

# 열/컬럼 선택하기 2
print('==== 컬럼 선택 ====\n')
print("C 컬럼: ", type(df[['C']]))
print(df[['C']]) # 컬럼 1개만 가능하고, str일 때만 가능함.


# 행/로우 선택하기- df.iloc[[정수 인덱스, ...]]
print('\n==== 로우 선택 ====\n')
print("여러 행 로우: ", type(df.loc[[2, 0, 1]]))
print(df.loc[[2, 0, 1]])

# 행/로우 선택하기 - df.loc[[라벨 인덱스, ...]]
print('\n==== 로우 선택 ====\n')
print("여러 행 로우: ", type(df.loc[['3rd']]))
print(df.loc[['3rd']])