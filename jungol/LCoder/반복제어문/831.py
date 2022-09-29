while True:
    width = int(input("Width = "))
    height = int(input("Height = "))
    Area = (width * height) / 2
    print("Triangle Area =",round(Area,1))

    go = input("Continue? ")

    if go == 'Y' or go == 'y' :
        pass
    elif go == 'N' :
        break