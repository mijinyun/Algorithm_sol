a = input().split(" ")
gender = a[0]
age = int(a[1])

if age >= 18 :
    if gender == 'M' :
        print('MAN')
    else :
        print('WOMAN')
else :
    if gender == 'M' :
        print('BOY')
    else :
        print('GIRL')