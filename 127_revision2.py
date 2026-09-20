def even_odd():
    n = int(input("enter the num: "))

    arr1 = []
    arr2 = []
    e_even = 0
    o_odd = 0
    for i in range(n):
        a = int(input(f"enter the value {i}: "))
        if a % 2 == 0:
            arr1.append(a)
        else:
            arr2.append(a)
    for i in arr1:
        e_even = e_even + i
    for i in arr2:
        o_odd = o_odd + i

    print(arr1,arr2)
    if e_even > o_odd:
        print("even sum is greater: ",e_even)
    else:
        print("odd sum is greater: ", o_odd)
even_odd()
        