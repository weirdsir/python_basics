words = list(input("Enter your sentence: ").split())
i = 0
for word in words:
    if len(word) > 10:
        print(i + 1, word[:10])
    else:
        print(i + 1, word)
    i = i + 1
