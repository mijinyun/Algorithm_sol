count = 0
count2 = 0

while True:
    num = int(input())
    count += 1

    if num == 0 :
        break
    elif num%3 == 0 or num%5 == 0 :
        count2 += 1
print(count - count2 - 1)