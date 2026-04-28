#  연산

import pandas as pd

# Series 인스턴스 생성
df1 = pd.DataFrame([[11, 22, 33], [10, 20, 30]])


# DF와 숫자 연산
print(f"df1 + 10 >>>\n{df1 + 10}\n")
print(f"df1 - 10 >>>\n{df1 - 10}\n")
print(f"df1 * 10 >>>\n{df1 * 10}\n")
print(f"df1 / 10 >>>\n{df1 / 10}\n")
print(f"df1 % 10 >>>\n{df1 % 10}\n")
print(f"df1 >= 10 >>>\n{df1 >= 25}\n")
print('===================================================')



df2 = df1 * 2
print(f"df1 + df2 >>>\n{df1 + df2}\n")
print(f"df1 - df2 >>>\n{df1 - df2}\n")
print(f"df1 * df2 >>>\n{df1 * df2}\n")
print(f"df1 / df2 >>>\n{df1 / df2}\n")
print(f"df1 % df2 >>>\n{df1 % df2}\n")
print(f"df1 >= df2 >>>\n{df1 >= df2}\n")
print('===================================================')


df2 = df1 * 2
print(f"df1 + df2 >>>\n{df1 + df2}\n")
print(f"df1 - df2 >>>\n{df1 - df2}\n")
print(f"df1 * df2 >>>\n{df1 * df2}\n")
print(f"df1 / df2 >>>\n{df1 / df2}\n")
print(f"df1 % df2 >>>\n{df1 % df2}\n")
print(f"df1 >= df2 >>>\n{df1 >= df2}\n")
print('===================================================')


print(f"df1.add(df2, fill_value = 0 >>>\n{df1.add(df2, fill_value = 0)}\n")
print(f"df1.sub(df2, fill_value = 0 >>>\n{df1.sub(df2, fill_value = 0)}\n")
print(f"df1.mul(df2, fill_value = 0 >>>\n{df1.mul(df2, fill_value = 1)}\n")
print(f"df1.div(df2, fill_value = 0 >>>\n{df1.div(df2, fill_value = 1)}\n")
