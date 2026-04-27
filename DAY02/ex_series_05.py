# Series 인스턴스 원소/요소 다루기
# >>> 읽기: 인스턴스 변수명[인덱스]
# >>> 변경: 인스턴스 변수명[인덱스] = 새로운 값

import pandas as pd
import func as f

# Series 객체 생성
data1 = [11, 33, 55, 77]

# Series 인스턴스 생성
sr1 = pd.Series(data1)
sr2 = pd.Series(data1, index = ['one', 'two', 'three', 'four'])

# 원소 값 읽기
print(f"1) sr1[0] -> {sr1[0]}, sr1[3] -> {sr1[3]}\n") # sr1[-1]과 같은 음수 인덱스는 지원하지 않음. 

# RangeIndex 외에 설정한 index가 존재하는 경우
# 인덱스 라벨과 위치인덱스 둘 다 존재
# 원소 접근이 사용자가 지정한 라벨이나 위치인덱스로 원소 접근 가능
# 나중에 iloc 메소드를 통해 위치인덱스로 접근해야함
print(f"2) sr2['one'] => {sr2['one']}, sr2['four'] => {sr2['four']}\n")
print(f"3) sr2[0] => {sr2[0]}, sr3[3] => {sr2[3]}\n") # 나중에는없어질 rangeindex로 찾아오기 기능
print(f"4) iloc 속성 사용: sr2[0] => {sr2.iloc[0]}, sr3[3] => {sr2.iloc[3]}\n") # iloc 속성을 사용해야함.
print("\n5) 인덱스 속성: ", sr2.index, '\n')

# 여러개 원소 다루기
print(f"6) 여러 개 요소 읽기: sr1[[0, 2]]\n>>>\n{sr1[[0, 2]]}\n")
print(f"7) 여러 개 요소 읽기: sr1[[0, 1, 2]]\n>>>\n{sr1[[0, 1, 2]]}\n")
print(f"8) 여러 개 요소 읽기: sr1[[0]]\n>>>\n{sr1[[0]]}\n")