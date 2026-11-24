class Lenght:
    def lenOfLastWord(self,s):
        i = len(s) - 1
        space = " "
        
        while i >= 0 and s[i] == space:
            i -= 1
        lenn = 0
        while i >= 0 and s[i] != space:
            lenn += 1
            i -= 1
        return lenn
l = Lenght()
print(l.lenOfLastWord('Hello World '))

                



