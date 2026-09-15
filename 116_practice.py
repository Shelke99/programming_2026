# def floyd_triangel(n):
#     nums = 1
#     for i in range(1, n + 1):
#         for j in range(1, i):
#             print(nums, end=" ")
#             nums += 1
#         print()

# floyd_triangel(4)

# Pyramid & Diamondi
# Print a centered star pyramid of height h, then extend it to a diamond.
# The trick is counting the spaces before the stars.
def Pyramid(h):
    s = " "
    r = "*"
    for i in range(1, h + 1):
       
        print(s * (h - i),end="")
            
        print(r * (2 * i - 1))
    # print()

    for i in range(h - 1, 0,-1):
        
        print(s * (h - i),end="")
            
        print(r * (2 * i - 1))    
                

    # print()

Pyramid(5)