class Solution:
    def paskelTriangle(self,triangle_rows):
        triangle = []
        for i in range(triangle_rows):
            row = [1]
            for j in range(1,i):
                value = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(value)
                # print(row)
            if i > 0:
                row.append(1)

            triangle.append(row)
        return triangle
sol = Solution()
print(sol.paskelTriangle(5))
