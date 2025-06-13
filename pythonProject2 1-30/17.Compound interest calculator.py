# Python compound interest calculator

# A=P(1+r/n) on t

# A = final amount
# P = initial principal balance
# r = interest rate
# t = number of time period elapsed

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount: "))
    if principle <0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate <0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if time <0:
        print("Time can't be less than or equal to zero")
    else:
        break
print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100),time)
print(f"Balance after {time} year/s: ${total:.2f}")