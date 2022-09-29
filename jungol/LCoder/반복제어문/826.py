list = ['Seoul','Washington','Tokyo','Beijing']

while True :
    print("""1. Korea
2. USA
3. Japan
4. China""")

    num = int(input('number? '))
    
    if 0 < num < 5 :
        print(list[num-1])
    else :
        print('none')
        break
