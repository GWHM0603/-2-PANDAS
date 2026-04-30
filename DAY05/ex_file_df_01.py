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
print("[8] 컬럼 인덱스는?\n", iris_df.columns, '\n')
print("[9] 행 인덱스를 컬럼 인덱스로 바꾼 결과는?\n", iris_df.index)
print("--------------------------------------------------------------")
print()
print()


# csv -> DF 로딩 및 기본 형태 확인 :: DATA_FIlE1
# 일부 컬럼만 가져오자
iris_df = pd.read_csv(DATA_FIlE1, usecols=[0, 1, 4])

# 기본 정보 확인
u.print_df('[10] 0, 1, 4번 컬럼만 추출한 CSV', iris_df)
print()

# 속성이 궁금하다!
print("[11] 컬럼 인덱스는?\n", iris_df.columns,'\n')
print("[12] DF의 형태 정보는?\n", iris_df.shape)
print("--------------------------------------------------------------")
print()
print()



# csv -> DF 로딩 및 기본 형태 확인 :: DATA_FIlE1
# 일부 행만 가져오자
# >>> skipfooter = 130 아래쪽 130개는 데이터 로딩안함
# >>> skiprows = 130 위쪽 130개는 데이터 로딩안함. 컬럼명도 버려서 주의

iris_df = pd.read_csv(DATA_FIlE1, skipfooter = 30, skiprows = 10, header = None)

# 기본 정보 확인
u.print_df('[13] 일부 행 제외한 CSV', iris_df)
print()

# 속성이 궁금하다!
print("[14] 컬럼 인덱스는?\n", iris_df.columns,'\n')
print("[15] DF의 형태 정보는?\n", iris_df.shape)
print("--------------------------------------------------------------")
print()
print()



# csv -> DF 로딩 및 기본 형태 확인 :: DATA_FIlE1
# 날짜/시간 컬럼 존재하는 데이터 파일
# >>> datetime64[ns] 형 변환 후 로딩:  parse_dates = [컬럼명] 매개변수
DATA_FILE4 ="../DATA/sample_data.csv"
csv_df = pd.read_csv(DATA_FILE4, parse_dates=['date'])

# 기본 정보 확인
u.print_df('[16] sample_data.csv', csv_df)
print()

# 속성이 궁금하다!
print("[17] 컬럼 인덱스는?\n", csv_df.columns,'\n')
print("[18] DF의 형태 정보는?\n", csv_df.shape, '\n')
print("[19] DF의 컬럼 타입은?\n", csv_df.dtypes.to_dict())
print("--------------------------------------------------------------")
print()
print()