freq = {}
nums = [1,2,3,4,5,6]
for num in nums:
    freq[num] = freq.get(num,0) + 1
print(freq)