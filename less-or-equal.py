def find_x(n, k, a):
    a.sort()
    
    if k == 0:
        if a[0] > 1:
            return a[0] - 1
        else:
            return -1
    
    if k == n:
        return a[-1]
    
    candidate = a[k - 1]
    
    if k < n and candidate == a[k]:
        return -1
    
    return candidate

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = find_x(n, k, a)
print(result)
