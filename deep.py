def main():
    user_i = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    n = user_i.lower()

    if user_i == "42":
        print("Yes")
    elif n == "forthy-two":
        print("Yes")
    elif n == "forthy two":
        print("Yes")
    else:
        print("no")

while True:
    main()