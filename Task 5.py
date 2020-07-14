from functools import reduce


def nlist(e1, e2):
    return e1 * e2


ulist = [el for el in range(100, 1001, 2)]
print(f"List{ulist}")
print(f"List with multiplicated numbers{reduce(nlist, ulist)}")
