## ===========================================
##          DataFrame 행과 열 다루기
## -------------------------------------------
## 행 선택
## >>> df변수명.iloc[정수 위치인덱스]
## >>> df변수명.loc[라벨 인덱스]
## 열 선택
## >>> df변수명[컬럼 이름]
## >>> df변수명.컬럼이름 -> 단, 컬럼이름이 str인 경우만 해당
## ===========================================

import pandas as pd 

datas = [ [11,33,55,77], 
            [ 2,22, 4,44] , 
            ['A',10,'B',0] ]

df = pd.DataFrame(datas, index = ['1st', '2nd', '3rd'], columns = ['A', 'B', 'C', 'D'])

print('[&&] DataFrame 기본 속성들\n')
print(f'[1] index: {df.index}\n')  
print(f'[2] columns: {df.columns}\n')  

# 열/컬럼 선택하기 1
print('==== 컬럼 선택 ====\n')
print("2번 컬럼: ", type(df['C']))
print(df['C'])

# 열/컬럼 선택하기 2
print('==== 컬럼 선택 ====\n')
print("3번 컬럼: ", type(df['D']))
print(df.D) # 컬럼 1개만 가능하고, str일 때만 가능함.


# 행/로우 선택하기 1 - iloc
print('\n==== 로우 선택 ====\n')
print("2번 로우: ", type(df.iloc[2]))
print(df.iloc[2])

# 행/로우 선택하기 2 - loc
print('\n==== 로우 선택 ====\n')
print("2번 로우: ", type(df.loc['3rd']))
print(df.loc['3rd'])