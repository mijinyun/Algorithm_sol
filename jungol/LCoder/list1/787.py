a1 = input("Element? ")
a2 = input("Element? ")
a3 = input("Element? ")
a4 = input("Element? ")
a5 = input("Element? ")
a6 = input("Element? ")
b = [a1,a2,a3,a4,a5,a6]
c = b[0::2]
d = b[1::2]
print(c + d)

# list[0::2] ---- 0번째 인덱스부터 2의 간격의 인덱스들의 요소들이 추출
# list[1::2] ---- 1번째 인덱스부터 2의 간격의 인덱스들의 요소들이 추출