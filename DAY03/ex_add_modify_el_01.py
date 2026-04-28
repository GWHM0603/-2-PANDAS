# DataFrame에서 행/열 추가/수정

# 모듈 로딩
import pandas as pd


# DataFrame 인스턴스 생성
dataDF = pd.DataFrame( 
    [[10, 20, 30, 40], [11, 22, 33, 44]], 
    columns = ['영', '일', '이', '삼'],
    index = ['row0', 'row1'] 
)


# Series 원소 추가/수정하기 
# 변수명[인덱스] = 원소값
# 변수명.loc[index] = 원소값 -> iloc는 불가능함(데이터가 없으므로 인덱스 설정이 불가함.).

print("\n[!!] 원본 DF >>>\n", dataDF, sep = '\n')
print()
print()


data_sr = dataDF.loc['row0']
print('==== DF에서 row0 추출 ====')
print("[1] 원본 row0 data_sr >>>\n", data_sr, sep = '\n')
print('=========================')
print()
print()


# 원소를 추가하자
data_sr['사'] = 100
data_sr.loc[5] = 55
print('==== 원소를 추가하자 ====')
print("[2] 추가 row0 data_sr >>>\n", data_sr, sep = '\n')
print('=========================')
print()
print()


# 원소를 수정/변경하자
data_sr['영'] = 7
data_sr.loc[5] = '오'
data_sr.iloc[5] = 999
print('==== 원소를 수정하자 ====')
print("[3] 수정 row0 data_sr >>>\n", data_sr, sep = '\n')
print('=========================')


# DF 행/열 추가, 행/열/원소 수정하기 
# 변수명[인덱스] = 원소값
# 변수명.loc[index] = 원소값 -> iloc는 불가능함(데이터가 없으므로 인덱스 설정이 불가함.).
