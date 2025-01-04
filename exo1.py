name=input('please enter you name')

if name=="vip" or name=="VIP" :
    print("Enjoy the show for free!")
else:
    nbtickets=input("How many tickets would you like to buy?")
    Prix=15.50
    total=Prix*nbtickets
    print("The total cost is",total)
    print("Enjoy your tickets!")