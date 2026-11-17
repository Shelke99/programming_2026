class Solution:
    def pascalTriangle(self,r):
        triangle = []
        for i in range(r):
            row = [1]
            for j in range(1,i):
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
            if i > 0:
                row.append(1)
            triangle.append(row)
        return triangle
sol = Solution()
print(sol.pascalTriangle(6))
