a = 10 #Gán giá trị 10 cho biến a, với 10 là kiểu số nguyên (int)
b = 20
c = a + b
str = "Toi la Hoang Quoc Bao" #Gan một chuỗi ký tự cho biến str => str có kiểu dữ liệu là string
dFloat = 8.5

#Lấy toàn bộ file trong thư viện decimal
from decimal import*
#Tổng chứ số của số decimal
getcontext().prec = 10

d = Decimal(100) / Decimal(3)

from fractions import*

frac1 = Fraction(5, 9)
frac2 = Fraction(4, 9)
result = frac1 + frac2

#In dong Hello World
print("Hello World!")
print("Phep cong a + b = ", c)
print(str)
print(dFloat)
print(d)
print(frac1)
print(result)
print(type(c))
print(type(str))
print(type(dFloat))
print(type(d))
print(type(frac1))
print(type(result))
