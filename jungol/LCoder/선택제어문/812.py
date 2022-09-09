year = int(input())

if ((year%400 == 0) | (( year%4 == 0 )&( year%100 != 0 ))) :
    print("leap year")
else :
    print('common year')