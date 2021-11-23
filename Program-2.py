a = int(input("type a : "))
output = []
j = 1
for i in range(a):
    output.append(str(j))
    j += 2
print(', '.join(output))