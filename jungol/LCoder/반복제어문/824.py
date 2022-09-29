sum=0
avg=0
count=0

while True:
    num = int(input())
    sum += num
    count += 1
    avg = sum/count
    if num >= 100 :
        break
print(sum)
print(round(avg,1))