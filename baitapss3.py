#Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $
s = input("Nhap chuoi: ")
for i in s:
    if i == s[0]:
        print(s.replace(i, '$'))
        break

#Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
s = input("Nhap chuoi: ")
m = int(input("Nhap m = "))
while True:
    if s == "" or m < 0 or m > len(s):
        print("Gia tri ban nhap khong hop le. Hay nhap lai.")
        s = input("Nhap chuoi: ")
        m = int(input("Nhap m = "))
        break
print(s.replace(s[m], ""))



#Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
s = input("Nhap chuoi: ")
print(s[::2])

'''Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,
        nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.'''
s = input("Nhap chuoi: ")
if len(s) < 2:
    print("")
elif len(s) == 2:
    print("Chuoi moi duoc sinh ra la: " + s[:])
else:
    print("Chuoi moi duoc sinh ra la: "+ s[:2] + s[-2:])


#Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím
s = input("Nhap chuoi: ")
print("Ky tu lon nhat cua chuoi: " + max(s))
print("Ky tu nho nhat cua chuoi: " + min(s))

#Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
s = input("Nhap chuoi: ")
print("Chuoi moi duoc dao: " + s.swapcase())