# def trapping_water():
#     w = [1,2,0,1,3,0,1,0,0,1]
#     ln = len(w)
#     water = 0
#     for i in range(ln):
#         l_side = 0
#         r_side = 0
#         for j in range(i-1,-1,-1):
#             l_side = max(l_side, w[j])
#         for k in range(i+1, ln):
#             r_side = max(r_side, w[k])
        
#         trap = min(l_side,r_side) - w[i]
#         if trap > 0:
#             water += trap

#     print(water)
# trapping_water()
def water_trapping():
    water = 0
    height = [1,0,0,2,0,3,2,1,0]
    sz = len(height)
    for i in range(sz):
        left_max = 0
        right_max = 0
        for j in range(i - 1,-1,-1):
            left_max = max(left_max, height[j])
        for j in range(i+1,sz):
            right_max = max(right_max, height[j])
        water += max(0,min(left_max, right_max) - height[i])
        # if trap > 0:
        #     water +=  - height[i]
    return water

print(water_trapping())