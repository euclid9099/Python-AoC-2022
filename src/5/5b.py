import functools
print("".join(list(map(lambda containers: "".join(containers).strip(), list(zip(*map(lambda line: line[1::4], open("5.input", "r").read().split("\n\n")[0].splitlines()[:-1])))))[pos[0] - 1][pos[1]] for pos in list(functools.reduce(lambda current, movement: (([position[0], position[1] + movement[0]]) if movement[1] == position[0] else (([movement[1], position[1]] if position[1] < movement[0] else [position[0], position[1] - movement[0]]) if movement[2] == position[0] else (position)) for position in current), map(lambda str_nrs: [int(str_nrs.split()[1]), int(str_nrs.split()[3]), int(str_nrs.split()[5])],(reversed(open("5.input", "r").read().split("\n\n")[1].splitlines()))), [[i, 0] for i in range(1, 1 + int((len(open("5.input", "r").readline()) + 1) / 4))]))))

"""
from bottom up
elements in sender:
index + count
elements in receiver:
change to sender[index] if index < count else index - count

1[0], 2[0], 3[0] + [1, 1, 2]
1[0 + 1], 1[0], 3[0] + [2, 2, 1]
2[0], 2[1], 3[0] + [3, 1, 3]
2[0], 2[1], 1[2] + [1, 2, 1]
2[1], 2[2], 1[1]

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1 -> [1, 2, 1]
move 3 from 1 to 3 -> [3, 1, 3]
move 2 from 2 to 1 -> [2, 2, 1]
move 1 from 1 to 2 -> [1, 1, 2]

[[N, Z], [D, C, M], [P]]
[[D, N, Z], [C, M], [P]]
[[], [C, M], [D, N, Z, P]]
[[C, M], [], [D, N, Z, P]]
[[M], [C], [D, N, Z, P]]

2[2], 2[1], 2[0]
2[1], 2[0], 1[0]
2[1], 2[0], 3[0]
1[1], 1[0], 3[0]
1[0], 2[0], 3[0]
M   , C   , D
"""