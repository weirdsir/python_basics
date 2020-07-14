og_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
changes = [og_list[el] for el in range(1, len(og_list)) if og_list[el] > og_list[el - 1]]
print(changes)
