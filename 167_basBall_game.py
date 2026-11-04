class Solution:
    def calPoint(self, operation):
        record = []
        for op in operation:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
sol = Solution()
print(sol.calPoint(["5","2","C","D","+","+","+","C","D","9"]))