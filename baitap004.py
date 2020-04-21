a = float(input('nhap do dai a:'))
b = float(input('nhap do dai b:'))
c = float(input('nhap do dai c:'))
if a <= 0 or b <= 0 or c <= 0:
    print('khong phai 3 canh cua 1 tam giac.Moi nhap lai')
elif a + b <= c or b + c <= a or c + a <= b:
    print('khong phai 3 canh cua t tam giac')
else:
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 +c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        print('do dai vua nhap tao thanh tam giac vuong')
    else:
        print('do dai vua nhap tao thanh tam giac khong phai tam giac vuong')

