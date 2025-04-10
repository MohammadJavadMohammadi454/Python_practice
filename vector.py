number = 5560737135
unique_digits = sorted(set(str(number)))  # تبدیل عدد به رشته، حذف ارقام تکراری، و مرتب‌سازی
unique_digits = [int(digit) for digit in unique_digits]  # تبدیل دوباره به اعداد

print(unique_digits)  # نمایش خروجی
