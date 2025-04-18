# نام فایل متنی شامل اعداد
file_path = "random_numbers (1).txt"

# خواندن اعداد از فایل و محاسبه میانگین
with open(file_path, "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

average = sum(numbers) / len(numbers)
print("average number is:", average)