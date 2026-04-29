# 통계 관련 메소드들
import sys
sys.path.append(R'C:\Users\KDT38\Desktop\KDT_14\[2]PANDAS\utils')
import pandas as pd
import utils as ut

# 데이터 준비
DATA_FILE = '../DATA/iris.csv'

# csv를 DataFrame으로 변환 저장
iris_df = pd.read_csv(DATA_FILE)


# 데이터 프레임 기본정보 확인
ut.data_info(iris_df)


# 통계 관련 메소드들
print("--------------------------------------------------------------")
# DataFrame에 전체 컬럼별 데이터 수 반환: count() -> axis = 0 기본값
# 각각의 행 단위로 계산 -> 결과값 열
cnt_sr = iris_df.count()
print(f"[1] cnt_sr(axis = 0) >>>\n{cnt_sr}")
print("--------------------------------------------------------------")
print()

print("--------------------------------------------------------------")
# DataFrame에 전체 컬럼별 데이터 수 반환: count() -> axis = 1 설정해봄
# 각각의 열 단위 -> 결괴값 행
cnt_sr = iris_df.count(axis=1)
print(f"[2] cnt_sr(axis = 1) >>>\n{cnt_sr}")
print("--------------------------------------------------------------")
print()


print("--------------------------------------------------------------")
# 행의 모든 값이 동일한 개수 반환: value_counts()
vcnt_sr = iris_df.value_counts()
print(f"[3] vcnt_sr >>>\n{vcnt_sr}")
print("--------------------------------------------------------------")
print()


print("--------------------------------------------------------------")
# 컬럼별 데이터의 개수 반환: value_counts()
# 특정 컬럼의 데이터별 개수: variety.value_counts()
vcnt_sr = iris_df.variety.value_counts()
print(f"[4-1] 컬럼별 데이터의 개수 반환 >>>\n{vcnt_sr}")
print("--------------------------------------------------------------")
vcnt_sr = iris_df['petal.width'].value_counts()
print(f"[4-2] 특정 컬럼의 데이터별 개수 >>>\n{vcnt_sr}")
print("--------------------------------------------------------------")
vcnt_sr = iris_df['variety'].value_counts()
print(f"[4-3] 특정 컬럼의 데이터별 개수 >>>\n{vcnt_sr}")
print("--------------------------------------------------------------")
print()


print("--------------------------------------------------------------")
# 컬럼별 데이터/값의 종류 개수 반환. 즉, 고윳값 반환: unique()
# DF에는 없음. Series에만 가능함. Series.unique()
# ex) varity 컬럼의 데이터/값 종류 => 고윳값
ret = iris_df['variety'].unique()
print(f"[5-1] varity 컬럼의 데이터/값 종류 => 고윳값 >>>\n{ret}\n원소 개수: {len(iris_df['variety'])}개")
print("--------------------------------------------------------------")
print()
print(f"[5-2] varity 컬럼의 고윳값별 원소 개수 >>>\n{iris_df['variety'].value_counts()}")
print("--------------------------------------------------------------")
print()

# ex) petal.width 컬럼의 데이터/값 종류 => 고윳값
ret = iris_df['petal.width'].unique()
print(f"[5-3] petal.width 컬럼의 데이터/값 종류 => 고윳값 >>>\n{ret}\n원소 개수: {len(iris_df['petal.width'])}개")
print("--------------------------------------------------------------")
print()
print(f"[5-2] petal.width 컬럼의 고윳값별 원소 개수 >>>\n{iris_df['petal.width'].value_counts()}")
print("--------------------------------------------------------------")
print()