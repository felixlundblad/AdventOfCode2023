with open('data/2.txt') as f:
    lines = f.readlines()

possible_games = 0

def minimum_color_product():
    sum = 0
    for line in lines:
        game = line.split(':')[-1].strip()
        game = game.split(';')
        minimum_colors = {}
        colors = {}
        for set in game:
            set = set.strip().replace(',', '').split(' ')
            for i in range(0, len(set), 2):
                colors[set[i+1]] = int(set[i])
            for key, value in colors.items():
                if key not in minimum_colors or minimum_colors[key] < value:
                    minimum_colors[key] = value
        power = 1
        for key, value in minimum_colors.items():
            power *= value
        sum += power
    return sum

print(minimum_color_product())    
