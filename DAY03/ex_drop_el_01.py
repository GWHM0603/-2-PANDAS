# DataFrame에서 행/열 삭제

# 모듈 로딩
import pandas as pd


# DataFrame 인스턴스 생성
dataDF = pd.DataFrame( 
    [[10, 20, 30, 40], [11, 22, 33, 44]], 
    columns = ['영', '일', '이', '삼'],
    index = ['row0', 'row1'] 
)


# DF 행/열 삭제하기 
# - 삭제할 원소 인덱스와 방향이 필요(axis -> 행: 0/index, 열: 1/columns)
# - 원본 사용 여부: inplace -> True 원본 사용, False 복사본 사용
# 1) 열/s컬럼 삭제
# 2) 행 삭제

print("\n[1] 원본 DF >>>\n", dataDF, sep = '\n')
print()
print()

# EX) '이' 컬럼을 삭제하자. 원본 유지
c_dataDF1 = dataDF.drop('이', axis = 1)
print('==== \'이\' 컬럼을 삭제하자. 원본 유지 ====')
print("[2] 삭제 후 원본 DF >>>\n", dataDF, sep = '\n')
print()
print("[3] 삭제 후 복사본 DF >>>\n", c_dataDF1, sep = '\n')
print('==========================================')
print()
print()

# EX) '이' 컬럼을 삭제하자. 원본 적용
c_dataDF2 = dataDF.drop('이', axis = 1, inplace = True)
print('==== \'이\' 컬럼을 삭제하자. 원본 적용 ====')
print("[4] 삭제 후 원본 DF >>>\n", dataDF, sep = '\n')
print()
print("[5] 삭제 후 복사본 DF >>>\n", c_dataDF2, sep = '\n')
print('==========================================')
print()
print()


dataDF = pd.DataFrame( 
    [[10, 20, 30, 40], [11, 22, 33, 44]], 
    columns = ['영', '일', '이', '삼'],
    index = ['row0', 'row1'] 
)

# EX) '삼' 컬럼을 삭제하자. 원본 유지
c_dataDF2 = dataDF.drop(columns ='이', axis = 1, inplace = False)
print('==== \'삼\' 컬럼을 삭제하자. 원본 유지 ====')
print("[6] 삭제 후 원본 DF >>>\n", dataDF, sep = '\n')
print()
print("[7] 삭제 후 복사본 DF >>>\n", c_dataDF2, sep = '\n')
print('==========================================')
print()
print()

# EX) '영', 삼' 컬럼을 삭제하자. 원본 유지
c_dataDF3 = dataDF.drop(columns = ['이', '삼'], axis = 1, inplace = False)
print('====  \'영\', \'삼\' 컬럼을 삭제하자. 원본 유지 ====')
print("[8] 삭제 후 원본 DF >>>\n", dataDF, sep = '\n')
print()
print("[9] 삭제 후 복사본 DF >>>\n", c_dataDF3, sep = '\n')
print('=================================================')
print()
print()


# EX)  'row1' 행 삭제하자. 원본 유지
c_dataDF4 = dataDF.drop('row1', axis = 0, inplace = False)
print('====  \'row1\' 행을 삭제하자. 원본 유지 ====')
print("[10] 삭제 후 원본 DF >>>\n", dataDF, sep = '\n')
print()
print("[11] 삭제 후 복사본 DF >>>\n", c_dataDF4, sep = '\n')
print('==========================================')
print()
print()

# EX)  'row1' 행 삭제하자. 원본 유지
c_dataDF5 = dataDF.drop('row1',axis = 'index', inplace = False)
print('====  \'row1\' 행을 삭제하자. 원본 유지 ====')
print("[12] 삭제 후 원본 DF >>>\n", dataDF, sep = '\n')
print()
print("[13] 삭제 후 복사본 DF >>>\n", c_dataDF5, sep = '\n')
print('==========================================')
print()
print()



# Series 행/열 삭제하기
# 1) 원소 삭제하기

dataDF = pd.DataFrame( 
    [[10, 20, 30, 40], [11, 22, 33, 44]], 
    columns = ['영', '일', '이', '삼'],
    index = ['row0', 'row1'] 
)

sr = dataDF.loc['row1']

c_sr = sr.drop(['영', '삼'])
print('시리즈 원소 삭제: ', c_sr)