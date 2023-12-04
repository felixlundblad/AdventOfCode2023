with open('data/1a.txt') as f:
    lines = f.readlines()

sum = 0

for line in lines:
    numbers = []
    for c in line:
        if c.isnumeric():
            numbers.append(c)
    sum += int(numbers[0]+numbers[-1])
    print(sum)

print('Final sum: ', sum)