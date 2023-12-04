with open('data/4.txt') as f:
    lines = f.readlines()
sum = 0
for line in lines:
    winning, numbers = line.split(': ')[-1].strip().split(' | ')
    winning = [x for x in winning.strip().split(' ') if x != '']
    numbers = [x for x in numbers.strip().split(' ') if x != '']
    number_of_winning = 0
    for number in numbers:
        if number in winning:
            if number_of_winning == 0:
                number_of_winning = 1
            else:
                number_of_winning = number_of_winning*2
    sum += number_of_winning

print(sum)