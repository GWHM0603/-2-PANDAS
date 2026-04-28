# DataFrame에서 행/열 선택

# 모듈 로딩
import pandas as pd


# DataFrame 인스턴스 생성
dataDF1 = pd.DataFrame( 
    [[10, 20, 30, 40], [11, 22, 33, 44]]
)

dataDF2 = pd.DataFrame( 
    [[10, 20, 30, 40], [11, 22, 33, 44]], 
    columns = ['영', '일', '이', '삼'],
    index = ['row0', 'row1'] 
)


# 생성된 인스턴스 확인하기
print("\ndataDF1 >>>", dataDF1, sep = '\n')
print()
print("\ndataDF2 >>>", dataDF2, sep = '\n')
print()
print()


# 행 선택하기 - loc, iloc 필순
# 1) 행 1개만 선택하기
# 2) 행 2개 이상 선택하기 - 인덱스 리스트
# 3) 행 2개 이상 선택하기 - 인덱스 슬라이싱
print('1.1)', dataDF2.loc['row0'])
print()
print('1.2)', dataDF2.iloc[0])
print()
print()
print('2.1)', dataDF2.loc[['row0', 'row1']])
print()
print('2.2)', dataDF2.iloc[[0, 1]])
print()
print()
print('3.1)', dataDF2.loc['row0': 'row1'])
print()
print('3.2)', dataDF2.iloc[0: 2])

