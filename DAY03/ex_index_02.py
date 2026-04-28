# 인덱스 관련 메소드 reindex()
# 기존 인덱스: 새롭게 재배치/재배열

# 모듈 로딩
import pandas as pd

# DF 인스턴스 생성 3행 4열
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

# 3행 4열 -> index를 one, two, three로
df.index=['one', 'two', 'three']
print('[2] df >>>\n', df, sep = '\n')
print()
print()

# 인덱스 재배열
new_df = df.reindex(['one', 'three', 'five'])
print('[3] new_df >>>\n', new_df, sep = '\n')
print()
print()

new_df = df.reindex(['two', 'five', 'one'])
print('[4] new_df >>>\n', new_df, sep = '\n')
print()
print()


# 컬럼 재배열 -> axis = 1 또는 columns
new_df = df.reindex(['A', 'D'], axis='columns')
print('[5] new_df >>>\n', new_df, sep = '\n')
print()
print()


new_df = df.reindex(columns = ['Z', 'A', 'D', 'F'])
print('[6] new_df >>>\n', new_df, sep = '\n')
print()
print()


new_df = df.reindex(columns = ['Z', 'A', 'D', 'F'], fill_value='%%')
print('[7] new_df >>>\n', new_df, sep = '\n')
print()
print()