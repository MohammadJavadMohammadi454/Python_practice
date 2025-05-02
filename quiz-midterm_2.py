# تابع بررسی عدد اول
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# تابع یافتن k‌امین عدد اول بعد از n
def kth_prime_after_n(k, n):
    count = 0
    number = n + 1
    while True:
        if is_prime(number):
            count += 1
            if count == k:
                return number
        number += 1

# اجرای برنامه
k = int(input("چندمین عدد اول بعد از n را می‌خواهید؟ k = "))
n = int(input("عدد شروع را وارد کنید: n = "))

prime = kth_prime_after_n(k, n)
print(f"{k}‌مین عدد اول بعد از {n} برابر است با: {prime}")