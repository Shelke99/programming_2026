def is_prime(num):
    for i in range(2,num):
        flag = 1
        if num % i == 0:
            flag = 0
            break
    if flag == 1:
        print("the given number is prime:",num)
    else:
        print("the given number is not prime:",num)

is_prime(19)

