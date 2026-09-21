def ransom_note(s1, s2):
    dic1 = {}
    
    
    for i in s2:
        if i in dic1:
            dic1[i] = dic1[i] + 1
        else:
            dic1[i] = 1
    for ch in s1:
        if ch in dic1 and dic1[ch] > 0:
            dic1[ch] = dic1[ch] - 1
            print(dic1)
        else:
            return False

    return True



    

    
print(ransom_note("aa","ab"))
