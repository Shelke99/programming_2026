def three_sum():
    # n = [-1,0,1,2,-1,-4]
    # n. sort()
    # ln = len(n)
    # ans = []

    # for i in range(0,ln-2):
    #     j = i + 1
    #     k = ln - 1
    #     while j < k:
    #         total = n[i] + n[j] + n[k]

    #         if total == 0:
    #             ans.append([n[i], n[j], n[k]])
    #             j += 1
    #             k -+ 1
    #         elif total > 0:
    #             k -= 1
    #         else:
    #             j += 1
    # print(ans)
    arr = [1,0,9,8,2,3,-5,-3,0]
    # arr.sort()
    # l = len(arr)
    # ans = []
    # for i in range(0,l-2):
    #     j = i + 1
    #     k = l - 1
    #     while j < k:
    #         sum = arr[i] + arr[j] + arr[k]
    #         if sum == 0:
    #             ans.append([arr[i],arr[j],arr[k]])
    #             j += 1
    #             k -= 1
    #         elif sum > 0:
    #             k -= 1
    #         else:
    #             j += 1
    arr.sort()
    ln = len(arr)
    ans = []
    total = 0
    for i in range(ln-2):
        j = i + 1
        k = ln - 1
        while i < k:
            total = arr[i] + arr[j] + arr[k]
            if total == 0:

                ans.append([arr[i],arr[j],arr[k]])
                j += 1
                k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1
    print(ans)

            
            

        
    # print(ans/)
three_sum()