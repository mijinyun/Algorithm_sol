list = []
a = input().split(" ")
b = input().split(" ")

for i in range(int(a[1])):
    list.append(int(a[0]))

for j in range(int(b[1])):
    list.append(int(b[0]))

print(list)