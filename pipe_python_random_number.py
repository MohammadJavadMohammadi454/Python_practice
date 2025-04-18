from pipe import select, where
from statistics import mean

file_path = "random.txt"

with open(file_path, "r") as file:
    lines = file | select(str.strip) | select(lambda line: line.split(','))
    
    # صاف کردن لیست تو در تو
    flat_numbers = [int(num.strip()) for sublist in lines for num in sublist if num.strip().isdigit()]

average = mean(flat_numbers)
print("average number is:", average)