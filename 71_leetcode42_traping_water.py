def trap_water(height):
    s = len(height)

    l_max = 0
    r_max = 0

    left = 0
    right = s - 1

    water = 0
    while left < right:
        if height[left] < height[right]:
            l_max = max(l_max, height[left])
            water += l_max - height[left]
            left += 1
        else:
            r_max = max(r_max,height[right])
            water += r_max - height[right]
            right -= 1
    return water
print(trap_water([0,1,2,1,3]))

