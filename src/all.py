import functools, itertools, math

print("Day 1a: " + str(max(map(lambda e: sum(map(lambda block: int(block), e.split("\n"))),open("1/1.input", "r").read().split("\n\n")))) + "\nDay 1b: " + str(sum(sorted(list(map(lambda e: sum(map(lambda block: int(block), e.split("\n"))),open("1/1.input", "r").read().split("\n\n"))))[-3:])) + "\nDay 2a: " + str(sum(map(lambda game: ((((ord(game.split(" ")[1]) - 86) % 3 - ord(game.split(" ")[0]) - 65)) % 3) * 3 + ord(game.split(" ")[1]) - 87, open("2/2.input", "r").read().splitlines()))) + "\nDay 2b: " + str(sum(map(lambda elem: 3 * (ord(elem.split(" ")[1]) - 88) + ((ord(elem.split(" ")[0]) - 65) + (ord(elem.split(" ")[1]) - 88) - 1) % 3 + 1, open("2/2.input", "r").read().splitlines()))) + "\nDay 3a: " + str(sum(map(lambda mismatch: mismatch - 96 if mismatch > 96 else mismatch - 38, map(lambda rucksack: ord(set(rucksack[:int(len(rucksack) / 2)]).intersection(set(rucksack[int(len(rucksack) / 2):])).pop()), open("3/3.input", "r").read().splitlines())))) + "\nDay 3b: " + str(sum(map(lambda badge: badge - 96 if badge > 96 else badge - 38, map(lambda rucksacks: ord(set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2])).pop()), list(open("3/3.input", "r").read().splitlines()[i:i+3] for i in range(0, len(open("3/3.input", "r").read().splitlines()), 3)))))) + "\nDay 4a: " + str(len([ranges for ranges in map(lambda line: list(map(lambda n: int(n), line.replace("-", ",").split(","))), open("4/4.input").read().splitlines()) if (ranges[0] >= ranges[2] and ranges[1] <= ranges[3]) or (ranges[0] <= ranges[2] and ranges[1] >= ranges[3])])) + "\nDay 4b: " + str(len([ranges for ranges in map(lambda line: list(map(lambda n: int(n), line.replace("-", ",").split(","))), open("4/4.input").read().splitlines()) if (ranges[0] >= ranges[2] and ranges[0] <= ranges[3]) or (ranges[0] <= ranges[2] and ranges[1] >= ranges[2])])) + "\nDay 5a: " + "".join(list(map(lambda containers: "".join(containers).strip(), list(zip(*map(lambda line: line[1::4], open("5/5.input", "r").read().split("\n\n")[0].splitlines()[:-1])))))[pos[0] - 1][pos[1]] for pos in list(functools.reduce(lambda current, movement: (([position[0], position[1] + movement[0]]) if movement[1] == position[0] else (([position[0], position[1] - movement[0]] if position[1] - movement[0] >= 0 else [movement[1], movement[0] - position[1] - 1]) if movement[2] == position[0] else (position)) for position in current), map(lambda str_nrs: [int(str_nrs.split()[1]), int(str_nrs.split()[3]), int(str_nrs.split()[5])],(reversed(open("5/5.input", "r").read().split("\n\n")[1].splitlines()))), [[i, 0] for i in range(1, 1 + int((len(open("5/5.input", "r").readline()) + 1) / 4))]))) + "\nDay 5b: " + "".join(list(map(lambda containers: "".join(containers).strip(), list(zip(*map(lambda line: line[1::4], open("5/5.input", "r").read().split("\n\n")[0].splitlines()[:-1])))))[pos[0] - 1][pos[1]] for pos in list(functools.reduce(lambda current, movement: (([position[0], position[1] + movement[0]]) if movement[1] == position[0] else (([movement[1], position[1]] if position[1] < movement[0] else [position[0], position[1] - movement[0]]) if movement[2] == position[0] else (position)) for position in current), map(lambda str_nrs: [int(str_nrs.split()[1]), int(str_nrs.split()[3]), int(str_nrs.split()[5])],(reversed(open("5/5.input", "r").read().split("\n\n")[1].splitlines()))), [[i, 0] for i in range(1, 1 + int((len(open("5/5.input", "r").readline()) + 1) / 4))]))) + "\nDay 6a: " + str(list(map(lambda text: list(i for i in range(4, len(text)) if len(set(text[i-4:i])) == 4),[open("6/6.input", "r").read()]))[0][0]) + "\nDay 6b: " + str(list(map(lambda text: list(i for i in range(14, len(text)) if len(set(text[i-14:i])) == 14),[open("6/6.input", "r").read()]))[0][0]) + "\nDay 7a: " + str(sum(i for i in list(map(lambda listing: functools.reduce(lambda cur_listing, val: cur_listing | {val: sum(n if type(n) is int else cur_listing[n] for n in cur_listing[val])}, listing, listing), [functools.reduce(lambda path_sizes, command: (path_sizes[0][:-1] if command.endswith("..\n") else path_sizes[0] + [command.split()[1]], path_sizes[1]) if command.startswith("cd") else (path_sizes[0], {"/".join(path_sizes[0]): list(map(lambda a: "/".join(path_sizes[0]) + "/" + a.split()[1] if a.startswith("dir") else int(a.split()[0]), command.splitlines()[1:]))} | path_sizes[1] ), open("7/7.input").read().split("$ ")[2:], (["~"], dict()))[1]]))[0].values() if i < 100000)) + "\nDay 7b: " + str(list(map(lambda list: [list[i] for i in range(len(list)) if list[i] > list[-1] - 40_000_000],[sorted(list(map(lambda listing: functools.reduce(lambda cur_listing, val: cur_listing | {val: sum(n if type(n) is int else cur_listing[n] for n in cur_listing[val])}, listing, listing), [functools.reduce(lambda path_sizes, command: (path_sizes[0][:-1] if command.endswith("..\n") else path_sizes[0] + [command.split()[1]], path_sizes[1]) if command.startswith("cd") else (path_sizes[0], {"/".join(path_sizes[0]): list(map(lambda a: "/".join(path_sizes[0]) + "/" + a.split()[1] if a.startswith("dir") else int(a.split()[0]), command.splitlines()[1:]))} | path_sizes[1] ), open("7/7.input").read().split("$ ")[2:], (["~"], dict()))[1]]))[0].values())]))[0][0]) + "\nDay 8a: " + str(len(list(map(lambda heightmap: list(heightmap[x][y] for x in range(0, len(heightmap)) for y in range(0, len(heightmap[0])) if heightmap[x][y] > min(max(heightmap[x][(y)+1:], default=-1), max(heightmap[x][:y], default=-1), max([row[int(y)] for row in heightmap][x + 1:], default=-1), max([row[int(y)] for row in heightmap][:x], default=-1))), [list(map(lambda line: list(map(lambda letter: int(letter), line.strip())), open("8/8.input", "r").readlines()))]))[0])) + "\nDay 8b: " + str(max(list(map(lambda heightmap: list((1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], [row[y] for row in heightmap][x+1:-1])))) * (1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], reversed(heightmap[x][1:y]))))) * (1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], reversed([row[y] for row in heightmap][1:x]))))) * (1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], heightmap[x][y+1:-1])))) for x in range(1, len(heightmap) - 1) for y in range(1, len(heightmap[0]) - 1)), [list(map(lambda line: list(map(lambda letter: int(letter), line.strip())), open("8/8.input", "r").readlines()))]))[0])) + "\nDay 9a: " + str(len(list(functools.reduce(lambda old, new: old if 2 > old[0][0] - new[0] > -2 and 2 > old[0][1] - new[1] > -2 else (((new[0] + int(math.copysign(1, old[0][0] - new[0])), new[1]), old[1] | {(x, new[1]) for x in range(old[0][0], new[0], int(math.copysign(1, new[0] - old[0][0])))[1:]}) if 2 > old[0][1] - new[1] > -2 else ((new[0], int(math.copysign(1, old[0][1] - new[1])) + new[1]), old[1] | {(new[0], y) for y in range(old[0][1], new[1], int(math.copysign(1, new[1] - old[0][1])))[1:]})), itertools.accumulate(open("9/9.input").readlines(), lambda head_tail, move: (head_tail[0] + (int(move[2:]) if move[0] in "RL" else 0) * (1 if move[0] == "R" else -1), head_tail[1] + (int(move[2:]) if move[0] in "UD" else 0) * (1 if move[0] == "D" else -1)), initial=(0,0)), ((0,0), {(0,0)}))[1]))) + "\nDay 9b: " + str(len(set(functools.reduce(lambda prev_node, current_node: functools.reduce(lambda old, new: old + [(i[0], i[1]) for i in itertools.zip_longest(range(old[-1][0], new[0], int(math.copysign(1, new[0] - old[-1][0]))), range(old[-1][1], new[1], int(math.copysign(1, new[1] - old[-1][1]))), fillvalue=(new[0] if abs(new[1] - old[-1][1]) > abs(new[0] - old[-1][0]) else new[1]))], prev_node, [(0,0)]), range(0,9), list(itertools.accumulate(open("9/9.input").readlines(), lambda head_tail, move: (head_tail[0] + (int(move[2:]) if move[0] in "RL" else 0) * (1 if move[0] == "R" else -1), head_tail[1] + (int(move[2:]) if move[0] in "UD" else 0) * (1 if move[0] == "D" else -1)), initial=(0,0))))))))
# for explanations on this monstrosity visit the specific solutions. this file is just a combination of the form "\nDay Na: " and whatever the corresponding oneliner was