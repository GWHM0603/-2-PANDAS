# file -> DataFrame 변환로딩
# 관련 함수들 >>>
# pandas.read_파일확장자() -> 엑셀은 확장자로 안되어 있음.
# pandas.read_csv() / pandas.read_excel() / pandas.read_json()

# 복습: DataFrame -> 행 인덱스 + 컬럼 인덱스 + 데이터
# 규칙: 파일의 첫 번째 줄 데이터는 컬럼이름으로 설정

import pandas as pd
import sys
sys.path.append(R'C:\Users\KDT38\Desktop\KDT_14\[2]PANDAS\utils')
import utils as u

# 데이터 파일 읽어오기
DATA_FIlE1 = '../DATA/iris.csv'
DATA_FIlE2 = '../DATA/iris_no_columns.csv'
DATA_FIlE3 = '../DATA/iris_space.csv'


# csv -> DF 로딩 및 기본 형태 확인 :: DATA_FIlE1
iris_df = pd.read_csv(DATA_FIlE1)

# 기본 정보 확인
u.print_df('[1] 첫 번째줄 컬럼명 있는 CSV', iris_df)
print()

# 속성이 궁금하다!
print("[2] 컬럼 인덱스는?\n", iris_df.columns)
print("--------------------------------------------------------------")
print()
print()




# csv -> DF 로딩 및 기본 형태 확인 :: DATA_FIlE2
# 첫 번째 줄이 데이터 -> 초기 컬럼 인덱스가 없는 csv
# header = None이 필요함.
iris_df = pd.read_csv(DATA_FIlE2, header = None)

# 컬럼 인덱스를 우리가 설정하자!
iris_df.columns = ['A', 'B', 'C', 'D', 'E']

# 기본 정보 확인
u.print_df('[3] 첫 번째줄 초기 컬럼 인덱스가 없는 CSV', iris_df)
print()

# 속성이 궁금하다!
print("[4] 컬럼 인덱스는?\n", iris_df.columns)
print("--------------------------------------------------------------")
print()
print()


# csv -> DF 로딩 및 기본 형태 확인 :: DATA_FIlE3

# 첫 번째 줄이 데이터 -> 초기 컬럼 인덱스가 없는 csv
# >>> header = None이 필요해

# 띄어쓰기로 구분된 csv
# >>> 공백 1개: sep 매개변수 설정 필요해
iris_df = pd.read_csv(DATA_FIlE3, header = None, sep = ' ')

# 컬럼 인덱스를 우리가 설정하자!
iris_df.columns = ['가', '나', '다', '라', '마']

# 기본 정보 확인
u.print_df('[5] 첫 번째줄 초기 컬럼 인덱스가 없고, 공백 1개로 구분된 CSV', iris_df)
print()

# 속성이 궁금하다!
print("[6] 컬럼 인덱스는?\n", iris_df.columns)
print("--------------------------------------------------------------")
print()
print()



# csv -> DF 로딩 및 기본 형태 확인 :: DATA_FIlE3

# 첫 번째 줄이 데이터 -> 초기 컬럼 인덱스가 없는 csv
# >>> header = None이 필요해

# 띄어쓰기로 구분된 csv
# >>> 공백 1개: sep 매개변수 설정 필요해

# 특정 컬럼을 행 인덱스로 바꾸고 싶네
# >>> index_col 매개변수 설정하자
iris_df = pd.read_csv(DATA_FIlE3, header = None, sep = ' ', index_col = 3)

# 기본 정보 확인
u.print_df('[7]] 첫 번째줄 초기 컬럼 인덱스가 없고, 공백 1개로 구분된 CSV', iris_df)
print()

# 속성이 궁금하다!
print("[8] 컬럼 인덱스는?\n", iris_df.columns)
print("[9] 행 인덱스를 컬럼 인덱스로 바꾼 결과는?\n", iris_df.index)
print("--------------------------------------------------------------")
print()
print()