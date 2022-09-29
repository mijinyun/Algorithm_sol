sum = 0
avg = 0
count = 0

while True:
    num = int(input())

    if num < 0 or num > 100 :
        break
    else :
        sum += num
        count += 1
        avg = sum /count

    
print('sum :',sum)
print('avg :',round((avg),1))