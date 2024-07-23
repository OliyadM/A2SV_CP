def is_possible_to_reduce(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] > 1:
            return "NO"
    return "YES"


t = int(input())
results = []
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    results.append(is_possible_to_reduce(arr))

for result in results:
    print(result)
