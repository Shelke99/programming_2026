def revision2():
    n = int(input("enter the value: "))
    marks = []
    A = 0
    b = 0
    c = 0
    f = 0
    num = n
    total = 0 
    avg = 0
    count = 0
    above_avg = []
    largest = float('-inf')
    smallest  = float('inf')

    for i in range(n):
        a = int(input(f"enter the student marks {i}: "))
        if (0 > a) or (a > 100):
            print("invalid marks...re-enter")
            break 
        marks.append(a)

    for i in range(len(marks)):
        if marks[i] >= 80:
            A += 1
        if 60 <= marks[i] < 80:
            b += 1
        if 40 < marks[i] < 60:
            c += 1
        if marks[i] < 40:
            f += 1
    # print()
        if largest < marks[i]:
            largest, _i = marks[i], i
        if smallest > marks[i]:
            smallest, _j  = marks[i],i
        total = total + marks[i] 

    print(f"heigest: {largest}, idx: {_i} , lowest: {smallest}, indx:{_j}")
    avg = total // num
    print(f"average: {avg}")
    for i in range(len(marks)):
        if marks[i] > avg:
            above_avg.append(i)
            count += 1
    print(f"indices: {above_avg},count: {count}")

        
        

            # print(f"the gread is A")
               
        # marks.append(a)
    print(marks)
revision2()