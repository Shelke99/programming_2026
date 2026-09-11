def strick_avg(n):
    h = float('-inf')
    s = float('inf')
    sum_ = 0
    avg = 0
    count = 0
    _i = 0
    _j = 0
    for i in range(len(n)):
        if n[i] > h:
            h, _i = n[i],i
        if n[i] < s:
            s, _j = n[i], i
        sum_ += n[i]

    avg = sum_ / len(n)
    for i in range(len(n)):
        if n[i] > avg:
            count +=1
        
    

    print(h, _i)
    print(s, _j)
    print(sum_)
    print(avg)
    print(count)

   
print(strick_avg([4, -1,9,3,9,2]))