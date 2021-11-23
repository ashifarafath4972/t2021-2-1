a = int(input("type a : "))
output = []
j = 1
for i in range(a):
    if i+1 == 1:
        output.append(str(j))
        j += 2
    elif (i+1) % 2 != 0:
        output.append(str(j))
        j += 2
        output.append(str(j))
        j += 2
print(', '.join(output))