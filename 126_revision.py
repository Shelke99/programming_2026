def frequent_occur():
    n = int(input("enter the num: "))
    arr = []
    arr2 = {}
    distinct = 0 
    frequent = 0
    most = float('-inf')
    for i in range(n):
        a = int(input(f"enter the value {i}: "))
        arr.append(a)

    for i in arr:
        # print(arr[i])
        if i in arr2:
            arr2[i] = arr2[i] + 1
        else:
            arr2[i] = 1
        
    for key, value in arr2.items():
        # print(i)
        if value >= 1:
            distinct += 1
        if most < value:
            most = value
            frequent = key
             
    print(frequent, distinct)
       
frequent_occur()