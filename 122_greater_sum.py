def greater_sum():
    arr = []
    even = []
    odd = []
    e_count = 0
    o_count = 0
    e_sum = 0
    o_sum = 0
    larger = 0
    n = int(input("enter the n: "))
    for i in range(n):
        a = int(input(f"enter the element in arrar {i}: "))
        # print(a)
        arr.append(a)
    for j in arr:
        if j % 2 == 0:
            even.append(j)
            e_count += 1
            e_sum += j
        if j % 2 != 0:
            odd.append(j)
            o_count += 1
            o_sum += j
    print(f"even_array : {even}, even_count: {e_count},even_sum: {e_sum}")
    print(f"odd_array: {odd}, odd_count: {o_count}, odd_sum: {o_sum}")
    if e_sum > o_sum:
        larger = e_sum - o_sum
        print(f"even sum is larger: {larger}")
    else:
        larger = o_sum - e_sum
        print(f"odd sum is larger: {larger}")


greater_sum()