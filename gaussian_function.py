import numpy as np
import matplotlib.pyplot as plt
import math

# تابع CDF گوسی به‌صورت دستی
def gaussian_cdf(x, mu=0, sigma=1):
    z = (x - mu) / (sigma * math.sqrt(2))
    return 0.5 * (1 + math.erf(z))

# پارامترها
mu = 0
sigma = 1

# دامنه گسترده‌تر با چگالی بیشتر
x = np.linspace(mu - 10*sigma, mu + 10*sigma, 2000)
cdf = [gaussian_cdf(xi, mu, sigma) for xi in x]

# رسم نمودار
plt.figure(figsize=(10, 6))
plt.plot(x, cdf, label='Manual Gaussian CDF', color='darkorange', linewidth=2)
plt.title('Gaussian CDF (Manual Implementation)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('CDF', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()