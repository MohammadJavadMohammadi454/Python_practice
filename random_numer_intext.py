# نام فایل متنی شامل اعداد
file_path = "random.txt"

# باز کردن فایل و محاسبه میانگین
with open(file_path, "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

average = sum(numbers) / len(numbers)

# چاپ میانگین
print("average number is:", average)