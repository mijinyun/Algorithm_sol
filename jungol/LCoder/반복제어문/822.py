num = int(input())
sum = 0

while num <= 100 :
    sum += num
    num -= 1
    if num == 0:
        break
print(sum)
    