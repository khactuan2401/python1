n = int(input('Nhap so nguyen duong n:'))

while n < 1000:

    if n > 0 and n <= 9:
        print('Tong chu so cua n la:')
        tong_chu_so = n
        print(tong_chu_so)
    elif n >= 10 and n <= 99:
        print('tong chu so cua n la:')
        tong_chu_so = n // 10 + n % 10
        print(tong_chu_so)
    elif n >= 100 and n < 1000:
        print('tong chu so cua n la:')
        tong_chu_so = n // 100 + (n - (n // 100) * 100) // 10 + n % 10
        print(tong_chu_so)
    else:
        print('so da nha khong thoa man ')
    break
print('So da nhap khong thoa man. Moi nhap lai n')


