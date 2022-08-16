A = []
T = 0
n = int(input("Nhập số tự nhiên n: "))
for i in range(n):
    num = int(input("Nhap so thu " + str(i + 1) + ": "))
    A.append(num)
    T = T + num
print("Dãy số đã nhập")
for i in range(n):
    print(A[i], end = " ")
print()
print("Tổng: ", T)
print("Trung bình: ", T/n)