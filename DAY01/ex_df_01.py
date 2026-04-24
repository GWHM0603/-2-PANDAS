# CSV 파일 -> DataFrame으로 읽기
# >>> 사용함수: read_csv("경로/파일명.csv", 옵션들...)

# [1] 모듈/패키지 로딩
import pandas as pd

# [2] csv 데이터 읽어오기
DATA_FILE = '../DATA/iris.csv'

# >>> DataFrame 형태로 저장
data_df = pd.read_csv(DATA_FILE)

# [3] 읽어온 데이터를 출력
print("전체 DataFrame 출력======================\n", data_df)
print()
print("속성들===================================\n")
print(f"index: {data_df.index}")
print(f"columns: {data_df.columns}")
print()
print(f"shape: {data_df.shape}")
print(f"dtypes: {data_df.dtypes}")




