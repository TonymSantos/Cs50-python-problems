def main():
    user_input = input("Tell me something!" )
    input_slow = user_input.replace(" ", "...")
    return print(input_slow)



while True:
    main()