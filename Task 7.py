def factorial(num):
    try:
        fact = 1
        for i in range(1, num):
            fact *= 1
            yield fact
    except ValueError:
        print("A number must be entered")


num = input("Enter a number: ")
for i in factorial(num):
    print(i)
