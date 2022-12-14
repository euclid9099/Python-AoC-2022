"""
[(head_tail[0][0] + ((1 if move[0] == "R" else -1) * int(move[2:])) if move[0] in "RL" else 0, head_tail[0][1] + ((1 if move[0] == "D" else -1) * int(move[2:])) if move[0] in "UP" else 0), head_tail[1]]
------H
-T-
---
(x, H.y) for x in range(T.x + 1, new[0], math.copysign(H.x - T.x))
[(x, H.y) for x in range(T.x, H.x, -1 if H.x - T.x < 0 else 1)[1:]]
[(H.x, y) for y in range(T.y, H.y, -1 if H.y - T.y < 0 else 1)[1:]]
"""
import itertools, functools, math
print(len(list(functools.reduce(lambda old, new: old if 2 > old[0][0] - new[0] > -2 and 2 > old[0][1] - new[1] > -2 else (((new[0] + int(math.copysign(1, old[0][0] - new[0])), new[1]), old[1] | {(x, new[1]) for x in range(old[0][0], new[0], int(math.copysign(1, new[0] - old[0][0])))[1:]}) if 2 > old[0][1] - new[1] > -2 else ((new[0], int(math.copysign(1, old[0][1] - new[1])) + new[1]), old[1] | {(new[0], y) for y in range(old[0][1], new[1], int(math.copysign(1, new[1] - old[0][1])))[1:]})), itertools.accumulate(open("9.input").readlines(), lambda head_tail, move: (head_tail[0] + (int(move[2:]) if move[0] in "RL" else 0) * (1 if move[0] == "R" else -1), head_tail[1] + (int(move[2:]) if move[0] in "UD" else 0) * (1 if move[0] == "D" else -1)), initial=(0,0)), ((0,0), {(0,0)}))[1])))