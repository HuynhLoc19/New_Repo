
from math import *
def Sum(n, i):
    if i==n+1:
        return 0
    S = Sum(n, i+1)
    return sqrt(i+S)
n = int(input('Nhập n: '))
print('Tổng dãy là: ', Sum(n, i=1))