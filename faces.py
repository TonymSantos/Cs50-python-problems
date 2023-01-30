def main():
    user_i = input("How are you today, use emoticons like ':)' or ':(' ")
    return user_i


def convert(user_i):
    user_i = main().replace(":)", "🙂").replace(":(","🙁")
    return user_i


while True:
    user_o = convert(main)
    print(user_o)