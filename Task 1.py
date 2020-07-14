from sys import argv


def payment():
    try:
        time, rate, addition = map(int, argv[1:])
        print(f"The salary equals to {(time * rate) + addition}")
    except:
        print("Program works with numbers only")


payment()
