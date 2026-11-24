class Rev:
    def revSrt(self, s):
        n = len(s)
        sz = n // 2
        for i in range(0,sz):
            s[i], s[n - i -1] = s[n - i - 1], s[i]
            return s
r = Rev()
print(r.revSrt(['h','e','l','l','o']))