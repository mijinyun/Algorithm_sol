odd=0
even=0

while True:
    num = int(input())
    if num > 0 :
        if num % 2 == 1 :
            odd += 1
        elif num % 2 == 0 :
            even += 1
    
    if num == 0 :
        print('odd :', odd)
        print('even :',even)
        break
