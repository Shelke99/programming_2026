def trapping_water():
    w = [1,2,0,1,3,0,1,0,0,1]
    ln = len(w)
    water = 0
    for i in range(ln):
        l_side = 0
        r_side = 0
        for j in range(i-1,-1,-1):
            l_side = max(l_side, w[j])
        for k in range(i+1, ln):
            r_side = max(r_side, w[k])
        
        trap = min(l_side,r_side) - w[i]
        if trap > 0:
            water += trap

    print(water)
trapping_water()