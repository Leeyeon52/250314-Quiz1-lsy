import numpy as np
import pandas as pd


A = pd.DataFrame(np.random.randint(0, 10, (2, 2)))
B = pd.DataFrame(np.random.randint(0, 10, (3, 3)))

print("DataFrame A \n", A)
print("DataFrame B \n", B)


# 함수를 이용해서 연산을 해보세요.
# NaN 값이 생기지 않도록 fill_value에 값을 넣어보세요
# A + B
add = A.add(B,fill_value=0)
print('A+B\n',add,'\n')
# A - B
sub = A.sub(B,fill_value=0)
print('A -B\n',sub,'\n')
# A * B
mul = A.mul(B,fill_value=1)
print('A*B\n',mul,'\n')
# A / B
div = A.div(B,fill_value=1)
print('A/B\n',div,'\n')

# 3 x 3 데이터프레임을 정렬해보세요.
C = pd.DataFrame([[1,3,5],[15,10,5],[2,8,5]], 
                 index = ['a','b','c'], 
                 columns = ['d','e','f'])

# c 행에 대해 오름차순 정렬
row_C = C.sort_values(by='d', axis=0)

# e 열에 대해 내림차순 정렬
column_C = C.sort_values(by='e', axis=0, ascending=False)

print("Row-wise sort:\n", row_C, '\n')
print("Column-wise sort:\n", column_C, '\n')

# 데이터 csv로 저장 및 불러오기
# index를 False로 설정하면 저장할 때 추가 인덱스를 달지 않습니다.
row_C.to_csv("data.csv", index=False)
load_C = pd.read_csv("data.csv")


print("Loaded CSV Data:\n", load_C)