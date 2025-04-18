import matplotlib.pyplot as plt
import random

# تعریف تبدیلات با احتمال
transforms = [
    {
        "prob": 0.40,
        "fx": lambda x, y: 0.31*x - 0.53*y + 0.89,
        "fy": lambda x, y: -0.46*x - 0.29*y + 1.04
    },
    {
        "prob": 0.15,
        "fx": lambda x, y: 0.31*x - 0.08*y + 0.22,
        "fy": lambda x, y: 0.15*x - 0.45*y + 0.34
    },
    {
        "prob": 0.45,
        "fx": lambda x, y: 0.55*x + 0.01,
        "fy": lambda x, y: 0.69*x - 0.20*y + 0.38
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

# الگوریتم  برای تولید صخره مرجانی
def draw_coral_reef(n=200000):
    x, y = 0, 0
    xs, ys = [], []
    for _ in range(n):
        t = choose_transform()
        x, y = t["fx"](x, y), t["fy"](x, y)
        xs.append(x)
        ys.append(y)
    return xs, ys

# رسم نقاط
xs, ys = draw_coral_reef()
plt.figure(figsize=(6, 6))
plt.plot(xs, ys, 'g.', markersize=0.5)
plt.axis('off')
plt.title("sakhre_marjani_fractal")
plt.show()