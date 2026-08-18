# Count digit frequency in an integer using loops and list/dictionary.
def digit_frq():
    n = int(input("enter the digit number:"))
    lst = [1,2,3,4,5,6,7,8,9,0]
    # d = str(n)
    count = {}
    for i in lst:
        print(lst[i])
        if n == lst[i]:
            count[i] += 1
    print(count)

            

digit_frq()

