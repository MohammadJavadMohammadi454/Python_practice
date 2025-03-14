# دریافت عدد دسیمال از کاربر
decimal_number = int(input("enter decimal format : "))

# تعریف یک متغیر خالی برای ذخیره عدد باینری
binary_number = ""

# استفاده از فرمول تقسیم مکرر بر 2
while decimal_number > 0:
    remainder = decimal_number % 2  # به دست آوردن باقیمانده
    binary_number = str(remainder) + binary_number  # افزودن باقیمانده به عدد باینری
    decimal_number = decimal_number // 2  # تقسیم بر 2 و گرفتن خارج قسمت

# نمایش نتیجه
print(f" binary format: {binary_number}")
