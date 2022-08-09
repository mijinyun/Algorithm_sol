arr =  list(input().split(" "))
L = len(arr)
ans = []
for i in range(L):
    if (i+1) % 3 == 0:
        ans.append(arr[i])
print(ans)