num = input().split(" ")
a = int(num[0])
b = int(num[1])
c = int(num[2])

arr = [a,b,c]
min_value = arr[0]

# [true_value] if [condition] else [false_value]

for val in arr :
    min_value = val if val < min_value else min_value

print(min_value)