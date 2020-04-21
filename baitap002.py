#Tính tổng S1 = 1 + x + x^2 + x^3 + ... + x ^ n
import math

x = int(input('Gia tri cua x='))
n = int(input('Gia tri cua n='))

S1 = 0
S2 = 0
S3 = 0

for i in range (0, n+1):
    S1 += x ** i
    S2 += (-x) ** i
    S3 += (x ** i) / math.factorial(i)
print(S1)
print(S2)
print(S3)
