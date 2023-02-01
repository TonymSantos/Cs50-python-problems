
x = int(input("Define X :"))
y = input("Define operator y :")
z = int(input("Define z :"))

if z == 0 and y == "/":
    print("Division by zero is undefined.")
    quit()


if y == "+":
    result = (x + z)
elif y == "-":
    result = (x - z)
elif y == "/":
    result = (x / z)
elif y == "*":
    result = (x * z)

print(result)