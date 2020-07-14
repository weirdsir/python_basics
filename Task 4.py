from random import randint

nlist = [randint(-10, 10) for i in range(20)]
chlist = [num for num in nlist if nlist.count(num) == 1]
print(f"Original list{nlist}")
print(f"Changed list{chlist}")
