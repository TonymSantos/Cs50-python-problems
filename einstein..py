def main():
    user_i = input("Tell me how many Kgs do you what the mass to be: " )
    user_o = int(user_i)*(300000000)**2
    return print("E=mc**2, so ",user_i,"Kgs, is",user_o,"Joules")

while True:
    main()