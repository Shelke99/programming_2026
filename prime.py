
# step = 10
# add = 0
# for i in range(2, n):
#     if n  % i == 0:
#         falg = 0
#         break
# if flag == 1:
#     print("the no is prime")
# else:
# #     print("is not prime")
# for j in range(2,step):
#     flag = 1
#     for i in range(2, j):
#         if j % i == 0:
#             flag = 0
#             break
#     if flag == 1:
#       print(j)
def is_prime(n):
    
    for i in range(2,n):
        flag = 1
        if n % i == 0:
            flag = 0
            break
    if flag == 1:
        print("is prime",n)
    else:
        print("not prime",n)
is_prime(11)