with open('data/4.txt') as f:
    lines = f.readlines()

wins_on_scratch = []
for line in lines:
    winning, numbers = line.split(': ')[-1].strip().split(' | ')
    winning = [x for x in winning.strip().split(' ') if x != '']
    numbers = [x for x in numbers.strip().split(' ') if x != '']
    number_of_winning = 0
    for number in numbers:
        if number in winning:
            number_of_winning += 1
    wins_on_scratch.append(number_of_winning)

amount_of_scratches = [1]*len(wins_on_scratch)
for i in range(len(wins_on_scratch)):
    for j in range(wins_on_scratch[i]):
        if i+j < len(wins_on_scratch):
            amount_of_scratches[i+j+1] += amount_of_scratches[i]

sum = 0
for scratches in amount_of_scratches:
    sum += scratches

print(sum)