# Print all even numbers between 1 and 100.
# def even_no(n):
#     for i in range(1,n + 1):
#         if i % 2 == 0:
#             print(i)


# even_no(100)
# Print the first n terms of the Fibonacci sequence.
# Display all prime numbers from 1 to 100.
# def all_prime(n):
    
#     for j in range(2, n):
#         flag = 1
#         for i in range(2, j):
#             if j % i == 0:
#                 flag = 0
#                 break
#         if flag == 1:
#             print("the number is prime",j)
#         # else:
#         #     print("is not prime",j)
        
# all_prime(100)

def is_palindrom():
    s = "A man, a plan a canal, Panama"
    sl = len(s)
    l = 0
    h = sl - 1
    print(s)
    while(l < h):
        if not s[l].isalnum():
            l += 1
            continue
        if not s[h].isalnum():
            h -= 1
            continue
        if s[l].lower() != s[h].lower():
            return False
        l += 1
        h -= 1         
    return True  
print(is_palindrom())      
        