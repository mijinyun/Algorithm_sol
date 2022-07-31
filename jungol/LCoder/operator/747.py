a = int(input())
b = int(input())
c = int(input())

if (a > b) & (a > c) & (a == b == c):
    print("True True")
elif (a > b) & (a > c) & ((a == b == c) != True):
    print("True False")
elif (((a > b) & (a > c)) !=True) & (a == b == c):
    print("False True")
else :
    print("False False")