def int_func(text):
    a = text.split()
    for word in a:
        r = word.capitalize()
        print(r, end=" ")


user_text = input("Enter a word or a sentence in lowercase")
int_func(user_text)
