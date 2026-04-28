#  연산

import pandas as pd

# Series 인스턴스 생성
sr1 = pd.Series([10, 20, 30, pd.NA])


# Series와 숫자 연산
print(f"sr1 + 10 >>>\n{sr1 + 10}\n")
print(f"sr1 - 10 >>>\n{sr1 - 10}\n")
print(f"sr1 * 10 >>>\n{sr1 * 10}\n")
print(f"sr1 / 10 >>>\n{sr1 / 10}\n")
print(f"sr1 % 10 >>>\n{sr1 % 10}\n")
print(f"sr1 >= 10 >>>\n{sr1 >= 25}\n")
print('===================================================')

# Series와 Series 연산
sr2 = pd.Series([5, 10, 15, 20])
print(f"sr1 + sr2 >>>\n{sr1 + sr2}\n")
print(f"sr1 - sr2 >>>\n{sr1 - sr2}\n")
print(f"sr1 * sr2 >>>\n{sr1 * sr2}\n")
print(f"sr1 / sr2 >>>\n{sr1 / sr2}\n")
print(f"sr1 % sr2 >>>\n{sr1 % sr2}\n")
print(f"sr1 >= sr2 >>>\n{sr1 >= sr2}\n")
print('===================================================')

# sr2 = pd.Series([5, 10, 15, 20], index = [0, 1, 3, 5])
# print(f"sr1 + sr2 >>>\n{sr1 + sr2}\n")
# print(f"sr1 - sr2 >>>\n{sr1 - sr2}\n")
# print(f"sr1 * sr2 >>>\n{sr1 * sr2}\n")
# print(f"sr1 / sr2 >>>\n{sr1 / sr2}\n")
# print(f"sr1 % sr2 >>>\n{sr1 % sr2}\n")
# print(f"sr1 >= sr2 >>>\n{sr1 >= sr2}\n")
# print('===================================================')

# Series 연산 관련 메소드 사용
# >>> 같은 인덱스가 없는 경우: NaN
# >>> 데이터가 NaN인 경우: NaN
# >>> fill_value 매개변수로 해결 가능 -> 무조건 0을 넣을 필요없음.
print(f"sr1.add(sr2, fill_value = 0 >>>\n{sr1.add(sr2, fill_value = 0)}\n")
print(f"sr1.sub(sr2, fill_value = 0 >>>\n{sr1.sub(sr2, fill_value = 0)}\n")
print(f"sr1.mul(sr2, fill_value = 0 >>>\n{sr1.mul(sr2, fill_value = 1)}\n")
print(f"sr1.div(sr2, fill_value = 0 >>>\n{sr1.div(sr2, fill_value = 1)}\n")

