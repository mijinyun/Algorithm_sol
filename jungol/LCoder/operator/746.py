a = True
b = True
c = False

print(a != True)
print(a & b)
print(a | b)
print(a & ( b | c))
print(a | (b & c))
print ((a!=True) | (b & (c != True)))