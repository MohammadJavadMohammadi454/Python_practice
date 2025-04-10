import random

# ایجاد بردار غیر تکراری از ارقام عدد 5560737135
number = 5560737135
unique_digits = list(set(str(number)))  # حذف ارقام تکراری
unique_digits = [int(digit) for digit in unique_digits]  # تبدیل به لیست اعداد صحیح

# تعداد عناصر مورد نیاز برای ماتریس 10×10
matrix_size = 10 * 10

# ایجاد دو بردار تصادفی از عناصر غیر تکراری
random_vector1 = [random.choice(unique_digits) for _ in range(matrix_size)]
random_vector2 = [random.choice(unique_digits) for _ in range(matrix_size)]

# تبدیل به ماتریس 10×10
matrix1 = [random_vector1[i:i+10] for i in range(0, matrix_size, 10)]
matrix2 = [random_vector2[i:i+10] for i in range(0, matrix_size, 10)]

# نمایش خروجی
print("بردار اولیه:", unique_digits)
print("\nMatrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)
