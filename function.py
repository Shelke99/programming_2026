def revert(n1):
    temp = 0
    ans = 0
    while n1 > 0:
        temp = n1 % 10
        ans = (ans * 10) + temp
        n1 = n1 // 10
    # print(ans)
    return ans

def is_prime(n2):
    i = 2
    flag = 1
    while i < n2:
        if n2 % i == 0:
            # print(i)
            flag = 0
            break

        i += 1
    if flag == 1:
        print(1)
        return 1
    else:
        return 0
 
    
if __name__ == "__main__":
    n6 = int(input("enter the number:"))
    n5 = revert(n6)
    print(n5)
    n3 = is_prime(n5)
    if n3 == 1:
        print("the number is prime")
    else:
        print("is not prime")


