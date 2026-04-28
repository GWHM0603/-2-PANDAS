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


# 원소 선택하기 -loc, iolc 필수
# 1) 원소 1개만 선택하기
# 2) 행 선택 후 열 지정
# 3) 여러 원소 선택
# 4) 응용
print('1.1)\n', dataDF2.iloc[0, 3])
print()
print('1.2)\n', dataDF2.loc['row0', '삼'])
print()
print()
print('2.1)\n', dataDF2.loc['row0']['삼'])
print()
print('2.2)\n', dataDF2.iloc[0].iloc[3])
print()
print('2.2)\n', dataDF2.iloc[0][3], 'Future Warning')
print()
print()
print('3.1)\n', dataDF2.loc['row0', ['일', '이', '삼']])
print()
print('3.2)\n', dataDF2.iloc[0, [1, 2, 3]])
print()
print('3.3)\n', dataDF2.loc[['row0', 'row1'], '일'])
print()
print('3.4)\n', dataDF2.iloc[[0, 1], 1])
print()
print()
print('4)\n', dataDF2.iloc[:, ::3],'\'영\'인덱스와 3칸 뒤 \'삼\'인덱스 출력 ')

