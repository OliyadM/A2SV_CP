# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def alternate(arr):
    result=[]
    for num in arr:
        if not result:
            result.append(num)
        elif num >=0:
            if result[-1]>=0:                
                if result[-1]<num:
                    result.pop()
                    result.append(num)
            else:
                result.append(num)
        else:
            if result[-1]>=0:                
                    result.append(num)
            else:
                if result[-1]<num:
                    result.pop()
                    result.append(num)
    return sum(result)
                






t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(alternate(arr))
