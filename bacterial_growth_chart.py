import matplotlib.pyplot as plt

# پارامترها
death_rate = 0.25     # احتمال مرگ
growth_factor = 2 * (1 - death_rate)  # رشد واقعی بعد از مرگ
start = 1             # شروع با یک باکتری
max_days = 50         # حداکثر تعداد روزها

# لیست برای ذخیره رشد باکتری‌ها
bacteria = [start]

# شبیه‌سازی رشد باکتری‌ها
for day in range(1, max_days + 1):
    next_population = bacteria[-1] * growth_factor
    bacteria.append(next_population)
    if next_population >= 1_000_000:
        print(f"Bacteria reached 1 million on day {day}")
        break

# رسم نمودار
plt.plot(bacteria, marker='o', color='blue')
plt.title("Bacterial Growth Curve")
plt.xlabel("Days")
plt.ylabel("Bacteria Count")
plt.grid(True)
plt.tight_layout()
plt.show()