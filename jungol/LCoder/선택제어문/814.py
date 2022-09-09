arr = [31,28,31,30,31,30,31,31,30,31,30,31]

num = int(input())

for i in range(len(arr)) :
    if num == (i+1):
        print(arr[i])