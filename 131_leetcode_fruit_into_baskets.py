def total_Fruit(fruits):
    sz = len(fruits)
    left = 0
    right = 0
    basket = {}
    max_window = 0
    for right in range(sz):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                basket.pop(fruits[left])
            left += 1
        max_window = max(max_window, right - left + 1)
    return max_window
print(total_Fruit([1,2,3,2,4,3,3]))