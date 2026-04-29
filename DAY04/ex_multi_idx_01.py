# 멀티인덱스
# 2개 이상의 데이터로 행/열 인덱스 구성한 것

import pandas as pd

# 데이터 준비 6x3
values = [ 
    [1,2,3], 
    [4,5,6], 
    [7,8,9],
    [10,11,12],
    [13,14,15], 
    [16,17,18] 
]

index_ = [ 
    ['row1','row1','row2','row2','row3','row3'],
    ['val1','val2','val1','val2','val2','val3'] 
]

# columns_ = ['col1', 'col2', 'col3']
columns_ = [ 
    ['A', 'B', 'B'],
    ['col1', 'col1', 'col2']
] 
## DF 생성
df = pd.DataFrame(values, columns=columns_, index=index_)
## MultiIndex 저장
mIndex = df.index
print(df, mIndex, sep = '\n\n')

## MultiIndex 속성들
print()
print(f'* levshape 속성: {mIndex.levshape}\n')
print(f'* names 속성: {mIndex.names}\n')
print(f'* nlevels 속성: {mIndex.nlevels}개\n')
print(f'* levels 속성: \n{mIndex.levels}\n')
print(f'* dtypes 속성: \n{mIndex.dtypes}\n')



# 행/열 선택하기
print("--------------------------------------------------------------")
# >>> 기본 행 선택하기
print('1. 기본 행 선택하기 >>>\n', df.loc[('row1', 'val1')])
print("--------------------------------------------------------------")
print()
print("--------------------------------------------------------------")
# >>> level0만 지정
print('2. level_0만 지정 >>>\n', df.loc['row1'])
print("--------------------------------------------------------------")
print()
print("--------------------------------------------------------------")
# >>> level1만 지정
# print('3. level1만 지정 >>>\n', df.loc['val1']) -> loc 속성에서 미지원함.\
print('3. level_1만 지정 >>>')
print(df.xs(key = 'val1', level = 1, drop_level=False))
print("--------------------------------------------------------------")
print()

print("--------------------------------------------------------------")
# >>> 열 추가
print('4. 열 추가 >>>')
df.loc[('A', 'col2')] = 0
df['C']= 0
print(df)
print("--------------------------------------------------------------")
print()


print("--------------------------------------------------------------")
# >>> 컬럼 인덱스 정렬
print('5. 컬럼 인덱스 정렬 (axis = 1, level = 0 >>>')
df = df.sort_index(axis = 1, level=0)
print(df, sep = '\n')
print("--------------------------------------------------------------")
print()


print("--------------------------------------------------------------")
# >>> 컬럼 인덱스 정렬
print('6. 컬럼 인덱스 정렬 (axis = 1, level = 1 >>>')
df = df.sort_index(axis = 1, level = 1)
print(df, sep = '\n')
print("--------------------------------------------------------------")
print()


print("--------------------------------------------------------------")
df.loc[('row1', 'val3'), :] = 0
print(df)

df  = df.sort_index(axis = 0, level = 0)
print(df)

df  = df.sort_index(axis = 0, level = 1)
print(df)
print("--------------------------------------------------------------")
