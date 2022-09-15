# 공백을 통해 인풋값을 공백으로 나눔
name = input().split(" ") 

# 공백으로 나누게 되면 배열형태로 들어오게된다.[' ', ' ']
FirstName = name[0]
LastName = name[1]

print(LastName,FirstName)
