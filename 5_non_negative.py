# 15.Print only non-negative values from user input, stop on a negative.
def non_negative():
    while True:
        values = int(input("enter the values:"))
        if values < 0:
            # continue
            print("you entered negative number")
            break
        print(values)
non_negative()
