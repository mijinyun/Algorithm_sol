a = int(input())
b = []
for i in range(1,16):
    if (i % a == 0):
        b.append(i)
print(b)

# 처음에 b = []를 하여 빈리스트를 만들고 for문을 돌면서 append(i)값을 해주며 리스트에 넣어줌!
