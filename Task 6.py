from itertools import count, cycle

# a
print("The program starts counting with the entered number. Enter # if you want to stop the program")
for i in count(int(input("Enter the number you want to begin with"))):
    print(i, end='')
    q = input()
    if q == "#":
        break
# b
print("The program repeats list's elements. Enter # if you want to stop the program")
uslist = input("Enter a list, dividing the elements with space").split()
el = cycle(uslist)
q = None

while q != "#":
    print(next(el), end="")
    q = input()
