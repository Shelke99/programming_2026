def fruitBasket(fruits):
    basket = {}
    right = 0
    left = 0 
    max_window = 0  
    for right in range(len(fruits)):

        basket[fruits[right]] = basket.get(fruits[right], 0) + 1
        # print(basket)
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                basket.pop(fruits[left])
            left += 1
        max_window = max(max_window, right - left + 1)
    return max_window

        
            

        
print(fruitBasket([1,2,3,2,2]))