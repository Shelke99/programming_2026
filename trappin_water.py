def traping_water():
    # w = [0,1,0,2,1,0,1,3,2,1,2,1]
    # ln = len(w)
    # water = 0
   
    # for i in range(0, ln):
    #     hl = 0
    #     hr = 0
    #     # left max
    #     for j in range(i-1, -1, -1):
    #         hl = max(hl,w[j])
    #         # print(hl)
    #     for j in range(i+1, ln):
    #         hr = max(hr,w[j]\
    #         # print(hr)

    #     water += max(0, min(hl,hr) - w[i])
    # print(water)

    w = [0,1,0,2,0,3,8,0,0,0,9]
    l = len(w)
    water = 0
    for i in range(0,l):
        hl = 0 
        hr = 0
        for j in range(i-1, -1,-1):
            hl = max(hl,w[j])
        for j in range(i+1, l):
            hr = max(hr,w[j])
        water += max(0,min(hl, hr)) - w[i]
    print(water)
        

traping_water()
