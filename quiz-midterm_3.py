import random
from itertools import combinations

# تولید 20 عدد تصادفی بین 1 تا 15
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 15))

print("لیست اعداد:", numbers)

# پیدا کردن کوچک‌ترین زیرمجموعه‌ای که مجموعش بین 50 تا 52 باشد
for r in range(1, len(numbers) + 1):
    all_combs = combinations(numbers, r)
    for comb in all_combs:
        s = sum(comb)
        if 50 <= s <= 52:
            print("زیرمجموعه پیدا شد:", comb)
            print("مجموع:", s)
            print("تعداد اعداد:", len(comb))
            exit()

print("زیرمجموعه‌ای با مجموع بین 50 تا 52 پیدا نشد.")