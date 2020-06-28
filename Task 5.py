inc = float(input("Enter company's income: "))
cost = float(input("Enter your company's costs: "))
if cost > inc:
    print("Unfortunately you work at a loss")
elif inc > cost:
    print("Congratulations, you are in profit")
    prof = inc - cost
    print(f"Your profit margin is {(prof * 100) / inc:.2f}%")
    wn = float(input("Enter the number of employees your company has: "))
    print(f"Profit per employee is {prof / wn:.2f}")
