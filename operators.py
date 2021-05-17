a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print (a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b) # 0 modulo: the remainder after integer divison

print()

for i in range(1, 4):
    print(i)

# This will return an error
#for i in range(1, a / b):
#    print(i)

# The two forward slashes will perform integer division and will work
for i in range(1, a // b):
    print(i)

print(a + b / 3 - 4 * 12)
print(a + (b/3) - (4 * 12))