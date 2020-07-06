def numsum(userList):
    sum1 = 0
    for num in userList:
        sum1 += int(num)
    print("Sum = ", sum1)


input_string = input("Enter a list of numbers separated by space ")
userList = input_string.split()
numsum(userList)
ans = input("Would you like to add more? Press # to stop adding numbers")

while ans != "#":
    userList = userList + ans.split()
    numsum(userList)
    ans = input("Would you like to add more? Press # to stop adding numbers")
    if ans == "#":
        print("Great, thanks for using this program!")