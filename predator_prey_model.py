import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# پارامترهای مدل شکار و شکارچی
alpha = 1.1   # نرخ رشد آهو
beta = 0.4    # نرخ شکار آهو توسط گرگ
delta = 0.1   # نرخ افزایش جمعیت گرگ از شکار
gamma = 0.4   # نرخ مرگ گرگ

# تابع معادلات لوتر-ولترّا
def lotka_volterra(t, z):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# دریافت ورودی از کاربر
x0 = float(input("تعداد اولیه آهوها را وارد کنید: "))
y0 = float(input("تعداد اولیه گرگ‌ها را وارد کنید: "))

# زمان شبیه‌سازی
t_span = (0, 50)
t_eval = np.linspace(*t_span, 1000)

# حل معادلات
sol = solve_ivp(lotka_volterra, t_span, [x0, y0], t_eval=t_eval)

# رسم نمودار جمعیت در زمان
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(sol.t, sol.y[0], label='آهو', color='green')
plt.plot(sol.t, sol.y[1], label='گرگ', color='gray')
plt.title('تغییرات جمعیت در زمان')
plt.xlabel('زمان')
plt.ylabel('جمعیت')
plt.legend()
plt.grid(True)

# رسم نمودار فازی: جمعیت گرگ در برابر آهو
plt.subplot(1, 2, 2)
plt.plot(sol.y[0], sol.y[1], color='purple')
plt.title('نمودار فازی: گرگ در برابر آهو')
plt.xlabel('جمعیت آهو')
plt.ylabel('جمعیت گرگ')
plt.grid(True)

plt.tight_layout()
plt.show()