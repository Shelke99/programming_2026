# 24. Keep reading input until a sentinel value (e.g., -99) is entered.
def infinite():
    while (n := int(input("enter the number: "))) != -99:
        print("You entered:", n)
    print('program stopped')  
infinite()