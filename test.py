n = int(input("Nhap so n: "))
S = 0
A = []
for i in range(n):
    num = int(input("Nhap so thu " + str(i+1) + ": "))
    A.append(num)
    S = S + num
    T = S/n
print(f"Tong cua day so la: {S}")
print("Trung binh cua day tren la " + str(T))
print("Day so tren la:")
for i in range(n):
    print(A[i],end = ",")