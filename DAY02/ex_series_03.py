# Series 인스턴스 생성
# >>> Pandas에서 1줄 데이터를 저장하는 타입
# >>> 구성: 원소식별 인덱스 + 데이터
# >>> 함수: Series(data, index, dtype)


import pandas as pd

# Series 객체 생성
data1 = [11, 33, 55, 77]

# Series 인스턴스 생성
sr1 = pd.Series(data1, index = ['a', 'b', 'c', 'd'], dtype = 'int8', name = 'data')

# Series 인스턴스 정보 확인 -> data, index, dtype 지정한 것
# Series 인스턴스/객체 변수명.속셩명
print(f"Series 속성들")
print(f"index -> {sr1.index}") # 원소 식별 번호
print(f"values ->{sr1.values}") # 원소에 저장된 데이터들
print(f"shape -> {sr1.shape}") # 1줄 시리즈의 형태. 튜프로 보기
print(f"nidm -> {sr1.ndim}") # 차원(1, 2, 3, ..., n) 정보
print(f"dtype => {sr1.dtype}") # 원소의 데이터 타입 정보
print(f"name => {sr1.name}") # 메타 정보/부가 정보로 이름 


# Series 형태 출력
print(f"\nSeries 형태 출력")
print(sr1,'\n')

# Series 인스턴스/객체 변수명.속셩명 = 새로운 값
sr1.index = ["하나", "둘", "셋", "넷"]
print(f"인덱스 수정한 Series 형태 출력")
print(sr1,'\n')


sr1.name = '점수'
print(f"name 수정한 Series 형태 출력")
print(sr1,'\n')


# sr1.values = [11, 22, 33, 44] -> 이런 식으로 직접 접근해서 데이터 값 수정이 불가능함.