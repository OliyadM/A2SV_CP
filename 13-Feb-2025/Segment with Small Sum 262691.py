# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

def longet(arr,k):
    n=len(arr)
    left=0
    cursum=0
    long=0
    for right in range(n):
        cursum+=arr[right]
        while cursum>k:
            cursum-=arr[left]
            left+=1
        long=max(long,right-left+1)
    return long

n,k =map(int,input().split())
arr=list(map(int,input().split()))
print(longet(arr,k))