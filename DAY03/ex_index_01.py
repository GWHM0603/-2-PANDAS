# 인덱스 관련 메소드 set_index()
# 인덱스 목적: 1행/관측값 추출하기 위한 용도. 유일한 값이고 반드시 존재해야 함.

# 모듈 로딩
import pandas as pd

# DF 인스턴스 생성
data = {
    'A': [10, 20, 30],
    'B': [8, 11, 7],
    'C': [9, 5, 8],
    'D': [11, 7, 4]
}

df = pd.DataFrame(data)
print('[1] df >>>\n', df, sep = '\n')
print()
print()

# 특정 컬럼 -> 행 인덱스로 설정
# df.set_index()
c_df = df.set_index('A')
print('[2] df >>>\n', df, sep = '\n')
print()
print()

print('c_df >>>\n', c_df, sep = '\n')
print()
print('[3] 새 인덱스: ', c_df.index, '\n')
print()
print('[4] 0번 원소: ', c_df.loc[10], '\n')
print()
print()

c_df = df.set_index(['A', 'B'])
print('[5] df >>>\n', df, sep = '\n')
print()
print()

print('[6] c_df >>>\n', c_df, sep = '\n')
print()
print(c_df.index)
print()

print('[7] 0번 원소\n', c_df.loc[(10, 8)], sep = '')
print()
print()




