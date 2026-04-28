# 정렬 관련 메소드
# 인덱스 기준 정렬: sort_index()
# 데이터 기준 정렬: sort_values()

# 모듈 로딩
import pandas as pd
import numpy as np
# 결측치/값이 없는 빈칸 -> missing value
# NaN, NaT, NA 등등
# DF 인스턴스 생성 3행 4열
data = {
    'Z': [10, np.nan, 30],
    'F': [8, 11, 7],
    'A': [9, 5, 8],
    'D': [11, 7, 4],
    'O': [np.nan, np.nan, np.nan] 
}

df = pd.DataFrame(data)
print('[1] df >>>\n', df, sep = '\n')
print()
print()

# 3행 4열 -> index를 one, two, five로
df.index=['ㅎ', 'ㄷ', 'ㄱ']
print('[2] df >>>\n', df, sep = '\n')
print()
print()


# 인덱스 정렬
new_df = df.sort_index()
print('[3] 오름차순 new_df >>>\n', new_df, sep = '\n')
print()
print()

new_df = df.sort_index(ascending=False)
print('[4] 내림차순 new_df >>>\n', new_df, sep = '\n')
print()
print()


new_df = df.sort_index(axis='columns')
print('[5] 오름차순 new_df >>>\n', new_df, sep = '\n')
print()
print()

new_df = df.sort_index(axis='columns',ascending=False)
print('[6] 내림차순 new_df >>>\n', new_df, sep = '\n')
print()
print()

df = pd.DataFrame(data)
print('[1] df >>>\n', df, sep = '\n')
print()
print()

# 컬럼 정렬
new_df = df.sort_values(by = 'Z')
print('[7] Z 기준 오름차순 new_df >>>\n', new_df, sep = '\n')
print()
print()

new_df = df.sort_values(by = 'Z', ascending=False)
print('[8] Z 기준 내림차순 new_df >>>\n', new_df, sep = '\n')
print()
print()


# 정렬 후 기존 인덱스 무시
new_df = df.sort_values(by = ['Z', 'A'],ignore_index=True)
print('[9] Z 기준 new_df >>>\n', new_df, sep = '\n')
print()
print()