import matplotlib.pyplot as plt
import random

# تعریف تبدیلات با احتمال
transforms = [
    {
        "prob": 0.02,
        "fx": lambda x, y: 0.0*x + 0.0*y + 0.5,
        "fy": lambda x, y: 0.0*x + 0.27*y + 0.0
    },
    {
        "prob": 0.15,
        "fx": lambda x, y: -0.14*x + 0.26*y + 0.57,
        "fy": lambda x, y: 0.25*x + 0.22*y - 0.04
    },
    {
        "prob": 0.13,
        "fx": lambda x, y: 0.17*x - 0.21*y + 0.41,
        "fy": lambda x, y: 0.22*x + 0.18*y + 0.09
    },
    {
        "prob": 0.70,
        "fx": lambda x, y: 0.78*x + 0.03*y + 0.11,
        "fy": lambda x, y: -0.03*x + 0.74*y + 0.27
    },
]

# انتخاب تصادفی یک تبدیل بر اساس احتمال
def choose_transform():
    r = random.random()
    total = 0
    for t in transforms:
        total += t["prob"]
        if r <= total:
            return t
    return transforms[-1]

# الگوریتم سرخس بار نزولی
def draw_fractal(n=400000):
    x, y = 0, 0
    xs, ys = [], []
    for _ in range(n):
        t = choose_transform()
        x, y = t["fx"](x, y), t["fy"](x, y)
        xs.append(x)
        ys.append(y)
    return xs, ys

# رسم نقاط
xs, ys = draw_fractal()
plt.figure(figsize=(6, 10))
plt.plot(xs, ys, 'g.', markersize=0.5)
plt.axis('off')
plt.title("sarakhs_fractal")
plt.show()