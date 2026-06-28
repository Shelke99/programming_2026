def numbers(n):
    for i in range(n):
        yield i
        # print()
        
for x in numbers(100):
    print(x)
# print(numbers(100))