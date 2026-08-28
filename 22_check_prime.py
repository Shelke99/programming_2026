#  Check prime (return 1 or 0, and print all primes up to a given number. 
def check_prime():
    num = int(input("enter the number:"))

    for i in range(2, num + 1):
        flag = 1

        for j in range(2,i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i)

            
        

print(check_prime())