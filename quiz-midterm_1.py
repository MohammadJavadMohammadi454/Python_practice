import matplotlib.pyplot as plt
import numpy as np

def draw_polygon_at(center_x, center_y, radius, n, rotation=0):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False) + rotation
    x = center_x + radius * np.cos(angles)
    y = center_y + radius * np.sin(angles)
    x = np.append(x, x[0])  # بستن شکل
    y = np.append(y, y[0])
    plt.plot(x, y, 'b-')
    plt.fill(x, y, alpha=0.2)
    return x[:-1], y[:-1]  # رئوس بدون تکرار آخر

def draw_tiled_polygons(n):
    if n <= 2:
        raise ValueError("تعداد اضلاع باید بزرگ‌تر از ۲ باشد.")

    radius = 1
    center_x, center_y = 0, 0

    plt.figure(figsize=(8, 8))
    # رسم شکل مرکزی
    vertices_x, vertices_y = draw_polygon_at(center_x, center_y, radius, n)

    # رسم شکل‌های اطراف (در هر ضلع یک بار تکرار)
    for i in range(n):
        # پیدا کردن وسط ضلع
        x1, y1 = vertices_x[i], vertices_y[i]
        x2, y2 = vertices_x[(i + 1) % n], vertices_y[(i + 1) % n]
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        # جهت بیرون شکل
        dx = mid_x - center_x
        dy = mid_y - center_y
        new_cx = mid_x + dx
        new_cy = mid_y + dy

        draw_polygon_at(new_cx, new_cy, radius, n)

    plt.gca().set_aspect('equal')
    plt.title(f'تکرار {n}-ضلعی منتظم در اطراف')
    plt.grid(True)
    plt.show()

# دریافت ورودی
try:
    n = int(input("تعداد اضلاع n را وارد کنید (بزرگ‌تر از ۲): "))
    draw_tiled_polygons(n)
except ValueError as e:
    print("خطا:", e)