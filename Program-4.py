input = [1,2,8,9,12,46,76,82,15,20,30]
output = {}
for i in range(9):
    output[i+1] = 0
for j in input:
    for k in range(9):
        if j % (k+1) == 0:
            output[k+1] += 1
print(output)