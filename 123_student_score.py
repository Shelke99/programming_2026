def student_score():
    marks = []
    A = 0
    B = 0
    C = 0
    F = 0
    heigest = float('-inf')
    lowest = float('inf')
    total = 0
    avg = 0
    indices = []
    n = int(input("enter the number of student: "))
    num = n 
    for i in range(n):
        a = int(input(f"enter the mark of student {i}: "))
        if (a <= 0 or a > 100):
            print("invalid mark {i}..please re-enter again ") 
            break
        else:
            marks.append(a)
            print(marks)
    for j in range(len(marks)):
        if marks[j] >= 80:
            A += 1
        elif 60 <= marks[j] <= 79:
            B += 1
        elif 40 <= marks[j] <= 59:
            C += 1
        elif marks[j] < 40:
            F += 1
        # else::
    print(f"gread A: {A}, B: {B}, C: {C}, F: {F}")
    for i in range(len(marks)):
        if heigest < marks[i]:
            heigest, _j = marks[i],i
        if lowest > marks[i]:
            lowest, _i = marks[i],i
        total += marks[i] 
    avg = total // n 
    for i in range(len(marks)):
        if marks[i] > avg:
            indices.append(i)

    print(f"heigest: {heigest},{_j}, lowest: {lowest},{_i}, total:{total} avg: {avg} indices above avg: {indices}")
    



        

student_score()

