def divide(a, b):
    try:
        c = a / b
        print(f"The answer is: {c:.2f}")
    except:
        try:
            print("This program does not divide by zero")
            print("Please enter different numbers")
            a = float(input())
            b = float(input())
            c = a / b
            print(f"The answer is: {c:.2f}")
        except:
            print("Please restart the program and stop entering inappropriate things")


print("Enter numbers you want to divide by each other: ")
try:
    a = float(input())
    b = float(input())
    divide(a, b)
except:
    print("Program works with numbers only")
