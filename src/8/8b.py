"""
max(heightmap[x][y+1:], default=-1), 
max(heightmap[x][:y], default=-1), 
max([row[y] for row in heightmap][x+1:], default=-1), 
max([row[y] for row in heightmap][:x], default=-1))
"""
import itertools
print(max(list(map(lambda heightmap: list((1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], [row[y] for row in heightmap][x+1:-1])))) * (1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], reversed(heightmap[x][1:y]))))) * (1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], reversed([row[y] for row in heightmap][1:x]))))) * (1 + len(list(itertools.takewhile(lambda tree: tree < heightmap[x][y], heightmap[x][y+1:-1])))) for x in range(1, len(heightmap) - 1) for y in range(1, len(heightmap[0]) - 1)), [list(map(lambda line: list(map(lambda letter: int(letter), line.strip())), open("8.input", "r").readlines()))]))[0]))