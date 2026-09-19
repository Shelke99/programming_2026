def about_range():
    nums = []
    count = 0 
    total_sum = 0
    largest = float('-inf')
    a = int(input("enter the first num: "))
    b = int(input("enter the second num: "))
    if a > b:
        a,b = b,a 
    for i in range(a, b):
        if (i % 4 == 1 and i % 6 == 1) and not (i % 5 == 0):
            nums.append(i)
            count += 1
            total_sum += i

    for i in nums:
        if largest < i:
            largest = i
    
    print(nums,count, total_sum, largest)

about_range()
