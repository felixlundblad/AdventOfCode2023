with open('data/2.txt') as f:
    lines = f.readlines()

possible_games = 0

def num_valid_games(color_limits):
    id_count = 0
    for line in lines:
        game = line.split(':')[-1].strip()
        id = int(line.split(':')[0].split(' ')[1])
        game = game.split(';')
        colors = {}
        bad_game = False
        for set in game:
            set = set.strip().replace(',', '').split(' ')
            for i in range(0, len(set), 2):
                colors[set[i+1]] = int(set[i])

            for key, value in color_limits.items():
                if key in colors and colors[key] > value:
                    bad_game = True
                    break
            if bad_game:
                break
        if not bad_game:
            id_count += id
    return id_count

print(num_valid_games({'red': 12, 'green': 13, 'blue': 14}))