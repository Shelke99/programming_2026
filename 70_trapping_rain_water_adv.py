def trap_rain_water(height):
    sz = len(height)


    lft = [0] * sz
    rgt = [0] * sz 
    mx = 0 
    
    for i in range(sz):
        mx = max(mx, height[i])
        lft[i] = mx 
    for i in range(sz-1,-1,-1):
        mx = max(mx, height[i])
        rgt[i] = mx


    water = 0
    
    for i in range(sz):
        water += min(lft[i], rgt[i]) - height[i]
    return water
print(trap_rain_water([0,1,2,1,3]))

        
             