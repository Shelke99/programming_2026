class Rev:
    def reverseString(self,s):
        st = len(s) - 1
        
        rev = []
        # print(st)
        while st >= 0:
            rev.append(s[st])

            st -= 1
        return rev
       
r = Rev()
print(r.reverseString(['h','e']))