def greet():
    greets = input("Choose a greeting:").lower()

    if "hello" in greets:
        prize = "$0"
    elif greets.startswith("h"):
        prize ="$20"
    else:
        prize ="$100"
    return print("Your prize is: " + prize)

while True:
    greet()