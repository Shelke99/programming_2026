# Calculate the sum of the series 1 + 1/2 + ... + 1/n
# def series(n):
#     total = 0

#     for i in range(1,n + 1):
#         total += 1 / i
#         print(total)
     
# series(10)

# Print uppercase ASCII characters and their codes.
# def ascc_code():
#     code = 0
#     for i in range(64, 91):
#         print(chr(i),'=',i)

# ascc_code()
# Create star patterns (square, triangle) of user-given height.
def pattern(n):
    for i in range(1, n):
        for j in range(i):
            print("*", end ="") 
        print()
pattern(10)