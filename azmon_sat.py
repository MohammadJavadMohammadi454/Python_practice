import scipy.stats as stats

# داده‌ها
mu = 1019  # میانگین
sigma = 209  # انحراف معیار
x = 820  # حداقل نمره برای پاس شدن

# محاسبه نمره Z
z_score = (x - mu) / sigma

# محاسبه احتمال نمره کمتر از ۸۲۰
probability = stats.norm.cdf(z_score)

# درصد داوطلبان که واجد شرایط نمی‌شوند
percentage = probability * 100

print(f"درصد داوطلبانی که واجد شرایط نمی‌شوند: {percentage:.2f}%")