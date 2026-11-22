class Solution:
    def mergeArray(self,n1,m, n2,n):
        i = m - 1
        j = n - 1
        w = (m + n) - 1
        n1 += [0] * n
        while j >= 0 :
            if (n2[j] < n1[i]):
                n1[w] = n1[i]
                i -= 1
            else:
                n1[w] = n2[j]
                j -= 1
            w -= 1
        return n1
sol = Solution()
print(sol.mergeArray([1,2,3],3, [2,5,6],3))