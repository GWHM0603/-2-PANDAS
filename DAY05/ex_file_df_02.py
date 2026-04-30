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
DATA_FILE1 = '../DATA/학생관리부.xlsx'

# EXCEL -> DF 로딩 및 기본 형태 확인 :: DATA_FILE1
# 엑셀 1행에 제목 
# 엑셀 2행에 공백
# >>> 컴퓨터상 0과 1 행은 삭제하자
# >>> 특정 컬럼을 행 인덱스로 사용하자.
excel_df = pd.read_excel(DATA_FILE1, header = 2, index_col='이름')

# 기본 정보 확인
u.print_df('[1] 첫 번째줄 컬럼명 있는 EXCEL', excel_df)
print()

# 속성이 궁금하다!
print("[2] 컬럼 인덱스는?\n", excel_df.columns, '\n')
print("[3] 행 인덱스는?\n", excel_df.index)
print("--------------------------------------------------------------")
print()
print()

# EXCEL -> DF 로딩 및 기본 형태 확인 :: DATA_FILE1
# 엑셀 파일에서 로딩할 시트 설정: sheet_name = 정수/문지열
excel_df = pd.read_excel(DATA_FILE1, header = 2, sheet_name= 1, index_col='이름', usecols = range(1, 7))

# 기본 정보 확인
u.print_df('[4] EXCEL의 두 번째 시트 설정', excel_df)
print()

# 속성이 궁금하다!
print("[5] 컬럼 인덱스는?\n", excel_df.columns, '\n')
print("[6] 행 인덱스는?\n", excel_df.index)
print("--------------------------------------------------------------")
print()


