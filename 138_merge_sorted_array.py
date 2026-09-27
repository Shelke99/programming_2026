def merge_array(nums1, n , nums2, m):
    i = n - 1
    j = m - 1
    p = (n + m) - 1
    while (j >= 0):
        if (i >= 0 and nums1[i] > nums2[j]):
            nums1[p] = nums1[i]
            i -= 1
            # p -= 1
        else:
            nums1[p] = nums2[j]
            j -= 1
        p -= 1
 
    return nums1
print(merge_array([1,2,3,0,0,0], 3, [2,5,6], 3))
