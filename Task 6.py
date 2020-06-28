a = int(input("Enter first day's result: "))
b = int(input("Enter the result you want to achieve: "))
i = 1
while a <= b:
    n = ((a * 10) / 100)
    a = a + n
    i = i + 1
print(f"That would take {i} days")
