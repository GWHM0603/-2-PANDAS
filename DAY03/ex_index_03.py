# 인덱스 관련 메소드 reset_index()

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


# 행 인덱스 => 매개변수 drop = False
new_df = df.reset_index()
print('[3] new_df >>>\n', new_df, sep = '\n')
print()
print()

# 행 인덱스
new_df = new_df.drop(columns = 'index')
print('[4] new_df >>>\n', new_df, sep = '\n')
print()
print()


# 행 인덱스
new_df = df.reset_index(drop= True)
print('[5] new_df >>>\n', new_df, sep = '\n')
print()
print()