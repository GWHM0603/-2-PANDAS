# csv 데이터 파일 -> dataFrame 변환 로딩
import pandas as pd

# 데이터 준비
DATA_FILE = '../DATA/iris.csv'

# csv를 DataFrame으로 변환 저장
iris_df = pd.read_csv(DATA_FILE)

# DF 기본 정보 확인하기
# >>> 요약 정보 반환
iris_df.info() 

# >>> 실제 데이터 확인하기. 기본이 5개. 출력기능 없어서 print해줘야 함
print('1\n', iris_df.head(), '\n')
print("###############################################################")
print() 

print('2\n', iris_df.head(2), sep = '') # 앞에 2개만 볼때
print("###############################################################")
print()

print('3\n', iris_df.head(2), iris_df.tail(2), sep = '\n') # 앞에 2개, 뒤에 2개 볼때
print("###############################################################")
print()

# >>> 컬럼별 통계정보 확인
print('4. 수치 컬럼별 정보', iris_df.describe(), sep = '\n')
print("###############################################################")
print()

print('5. 모든 컬럼별 정보', iris_df.describe(include='all'), sep = '\n')
print("###############################################################")
print()


# >>> describe()/head()/tail() 메소드 결과는 저장 후 활용가능
desc_df = iris_df.describe()
print('describe()/head()/tail() 메소드 결과는 저장 후 활용가능')
print(type(desc_df), desc_df.index, desc_df.columns, sep = '\n')
print("###############################################################")
print()
