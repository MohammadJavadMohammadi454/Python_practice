import matplotlib.pyplot as plt
import random
import math

# تعریف رئوس مثلث
R = (0, 0)
G = (1, 0)
B = (0.5, math.sqrt(3)/2)
vertices = [R, G, B]

# نقطه شروع
current_point = R

# تعداد تکرارها
n = 10000

# لیست برای ذخیره نقاط تولید شده
points_x = []
points_y = []

# اجرای بازی آشوب
for _ in range(n):
    chosen_vertex = random.choice(vertices)
    current_point = (
        (current_point[0] + chosen_vertex[0]) / 2,
        (current_point[1] + chosen_vertex[1]) / 2
    )
    points_x.append(current_point[0])
    points_y.append(current_point[1])

# رسم نتیجه
plt.figure(figsize=(6, 6))
plt.scatter(points_x, points_y, s=0.1, color="purple")
plt.axis("equal")
plt.title("triangle_fractal")
plt.show()