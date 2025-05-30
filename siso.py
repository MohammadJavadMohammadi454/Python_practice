import numpy as np
from scipy.signal import StateSpace, lsim
import matplotlib.pyplot as plt

def get_matrix_elements(rows, cols, name):
    print(f"\nلطفاً درایه‌های ماتریس {name} ({rows}x{cols}) را وارد کنید:")
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix[i,j] = float(input(f"{name}[{i+1},{j+1}]: "))
    return matrix


n = int(input("لطفاً بعد سیستم (تعداد متغیرهای حالت) را وارد کنید (n): "))



print(f"\nسیستم SISO با مشخصات زیر ایجاد می‌شود:")
print(f"- ماتریس A: {n}x{n} (سیستم)")
print(f"- ماتریس B: {n}x1 (ورودی)")
print(f"- ماتریس C: 1x{n} (خروجی)")
print(f"- ماتریس D: 1x1 (پیش‌خور)")

A = get_matrix_elements(n, n, "A")
B = get_matrix_elements(n, 1, "B")
C = get_matrix_elements(1, n, "C")
D = get_matrix_elements(1, 1, "D")


sys = StateSpace(A, B, C, D)


t = np.linspace(0, 10, 1000)
u = np.ones_like(t)


t, y, x = lsim(sys, u, t, X0=np.zeros(n))

plt.figure(figsize=(10, 6))
plt.plot(t, y, 'b', linewidth=2, label='پاسخ خروجی')
plt.title('پاسخ سیستم به ورودی پله واحد', fontsize=14)
plt.xlabel('زمان (ثانیه)', fontsize=12)
plt.ylabel('خروجی', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.show()

print("\nخلاصه سیستم ایجاد شده:")
print(f"ابعاد سیستم: n = {n}")
print("ماتریس A:\n", A)
print("ماتریس B:\n", B)
print("ماتریس C:\n", C)
print("ماتریس D:\n", D)