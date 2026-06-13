# def is_prime(num):
#     for i in range(2, num):
#         flag = 1
#         if num % i == 0:
#             flag = 0
#             break
#     if flag == 1:
#         print(num,"is prime")
#     else:
#         print("not p")
# is_prime(510)
# def reverse_num(num):
#     ans = 0
#     while num > 0:
#         temp = num % 10
        
#         ans = (ans * 10) + temp
#         num = num // 10
#         # print(ans)
#     return ans
# print(reverse_num(123))
# def get_userinput():
#     number = []
#     while True:
#         n = (input("enter the integer num: "))
#         if n.lower() == 'done':
#             break
#         try:
#             num = int(n)
#             number.append(num)
#         except:
#             print("please add correct number: ")
#     return number
# def filter_num(number):
#     even_num = [item for item in number if item % 2 ==0]
#     return even_num
# if __name__ == '__main__':
#     number = get_userinput()
#     even = filter_num(number)
#     print(even)
# def trapping_water():
#     w = [2,0,0,3]
#     water = 0
#     sz = len(w)
#     for i in range(sz):
#         l = 0
#         r = 0
#         for j in range(i-1,-1,-1):
#             l = max(l,w[j])
#         for j in range(i+1, sz):
#             r = max(r,w[j])
#         water += max(0, min(l,r) - w[i])
#     return water
# print(trapping_water())
# def no_negative():
#     while True:
#         n = int(input('enter the num'))
#         if n >= 0:
#             print(n,'is positive integer ')
#         else:
#             print("you enter negative num")
#             break
# no_negative()

# def divisor(n):
#     for i in range(2,n):
#         if n % i == 0:
#             print(i)
#             break
# divisor(11)

# def avg_of_pos():
#     temp = 0
#     count = 0
#     avg = 0
#     while True:
        
        
        
#         num = float(input("enter the num: "))
        
#         if num > 0:
#             temp += num
#             print(temp)          
#             count += 1    
#             print(count)       
#         else:
#             break
#         avg = temp // count
#         print('ans',avg)
# avg_of_pos()

# def table(n):
#     for i in range(1,n):
#         for j in range(1,n):
#             print(i * j)
# table(11)
