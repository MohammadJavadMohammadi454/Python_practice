income = int(input("Enter income: "))
if income < 0:
    rate = 0.000
elif income <= 8925:        # include 8925
    rate = 0.100
elif income <= 36250:       # include 36250
    rate = 0.150
elif income <= 87850:       # include 87850
    rate = 0.230
elif income <= 183250:      #include 183250
    rate = 0.280
elif income <= 398350:      # include 398350
    rate = 0.330
elif income <= 400000:      # include 400000
    rate = 0.350
else:
    rate = 0.396
print(rate)
