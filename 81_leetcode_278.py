FIRST_BAD = 4
def isBadVersion(version):
    return version >= FIRST_BAD

def bad_version(n):
    lo = 1
    hi = n 
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
TotalVersion = 6
print(bad_version(TotalVersion))