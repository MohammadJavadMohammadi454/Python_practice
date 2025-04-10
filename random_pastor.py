import random

# تعریف کارت‌های بازی
suits = ['♥️', '♦️', '♣️', '♠️']  # خال‌ها: دل، خشت، گشنیز، پیک
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # مقادیر کارت‌ها

# ایجاد لیست کارت‌ها
deck = [value + " " + suit for suit in suits for value in values]

# برد زدن (Shuffle)
random.shuffle(deck)

# نمایش کارت‌های برد زده‌شده
print("کارت‌های برد زده‌شده:")
for card in deck:
    print(card)
