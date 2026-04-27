# Series 인스턴스 생성
# >>> List, Tuple, Set, Str 데이터 -> Series
# >>> Dict 데이터 -> Series

import pandas as pd
import func as f

# Series 객체 생성
data1 = [11, 33, 55, 77]
data2 = 111, 333, 222
data3 ={1, 4, 7, 1, 9, 8, 1, 3}
data4 = {'A': 90, 'B': 80}
data5 ="Good"

# Series 인스턴스 생성
# sr1 = pd.Series(data1, index = ['a', 'b', 'c', 'd'], dtype = 'int8', name = 'data')
sr1 = pd.Series(data1)
sr2 = pd.Series(data2)
# sr3 = pd.Series(data3)  # set은 항상 순서가 바뀌므로 인덱스를 할당할 수 없음 
sr4 = pd.Series(data4) # dict는 키값이 항상 인덱스로 할당됨.
sr5 = pd.Series(data5)



f.print_info(sr1, 'sr1')
f.print_info(sr2, 'sr2')
# f.print_info(sr3, 'sr3')  # set은 항상 순서가 바뀌므로 인덱스를 할당할 수 없음
f.print_info(sr4, 'sr4')
f.print_info(sr5, 'sr5')