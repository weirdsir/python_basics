n = int(input("Enter a number of seconds: "))
s = n % 60
m = n // 6
h = m // 60
m = m % 60
d = h // 24
h = h % 24

print(f"The number yove equals to {s} seconds, {m} minutes, {h} hours, and {d} days")
print(f"{h}:{m}:{s}")
