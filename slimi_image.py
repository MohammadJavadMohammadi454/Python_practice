import numpy as np
import matplotlib.pyplot as plt

def custom_flower(x_offset, y_offset, scale=1, color='royalblue'):
    t = np.linspace(0, 2*np.pi, 1000)
    r = 0.5 + 0.5 * np.sin(7 * t) * np.cos(3 * t)
    x = scale * r * np.cos(t) + x_offset
    y = scale * r * np.sin(t) + y_offset
    plt.plot(x, y, color=color, linewidth=1.8)

def draw_custom_islami():
    plt.figure(figsize=(10, 10))
    plt.axis('equal')
    plt.axis('off')
    
    # ترسیم گل مرکزی
    custom_flower(0, 0, scale=2.5, color='darkgreen')

    # ترسیم گل‌های دایره‌ای اطراف
    for i in range(8):
        angle = np.pi * i / 4
        x = 4 * np.cos(angle)
        y = 4 * np.sin(angle)
        custom_flower(x, y, scale=1.2, color='darkred')
    
    # ترسیم گل‌های کوچک در زاویه‌های خاص (طرح خاص)
    angles = [np.pi/6, np.pi/3, 5*np.pi/6, 4*np.pi/3]
    for angle in angles:
        x = 2.5 * np.cos(angle)
        y = 2.5 * np.sin(angle)
        custom_flower(x, y, scale=0.9, color='goldenrod')

    plt.title("طرح اسلیمی اختصاصی", fontsize=16)
    plt.show()

# اجرای طرح
draw_custom_islami()