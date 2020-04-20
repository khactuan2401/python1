# coding=utf-8
import math

a, b, c = float(input('Nhập số a=')), float(input('Nhập số b=')), float(input('Nhập số c='))

if a == 0:
    if b == 0:
        if c == 0:
            print('phương trình có vô số nghiệm')
        else:
            print('phương trình vô nghiệm')
    else:
        if c == 0:
            print('phương trình có vô số nghiệm')
        else:
            print('phương trình có nghiệm duy nhất x=', -c/b)

elif a != 0 and b == 0 and c == 0:
        print('phương trình có nghiệm x=', 0)
elif a != 0 and b == 0 and c < 0:
        print('phương trình có 2 nghiệm phân biệt:')
        print('x1=', float(math.sqrt(c / a)))
        print('x2=', float(-math.sqrt(c / a)))
elif a != 0 and b == 0 and c > 0:
        delta1 = -4 * a * c
        print('phương trình có 2 nghiệm phức:')
        print('x3=', complex(0, math.sqrt(math.fabs(delta1))))
        print('x4=', complex(0, -math.sqrt(math.fabs(delta1))))
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        print('phương trình có 2 nghiệm phân biệt:')
        print('x1=', float((-b - math.sqrt(delta)) / (2 * a)))
        print('x2=', float((-b + math.sqrt(delta)) / (2 * a)))
    else:
        print('phương trình có 2 nghiệm phức:')
        print('x3=', complex((-b / 2 * a ), math.sqrt(math.fabs(delta)) / (2 * a)))
        print('x4=', complex((-b / 2 * a ), -math.sqrt(math.fabs(delta)) / (2 * a)))
