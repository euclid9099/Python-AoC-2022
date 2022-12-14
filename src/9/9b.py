"""
def visualize(points):
    f = open("path_visual", "w")
    points = sorted(points, key=lambda tup: tup[1] * 1000 + tup[0])
    min_x = min(tup[1] for tup in points)
    cursor = (min_x,points[0][1])
    f.write(str(points) + "\n\n\n")
    for p in points:
        while cursor[1] < p[1]:
            f.write("...\n")
            cursor = (min_x, cursor[1] + 1)
        while cursor[0] < p[0]:
            f.write(".")
            cursor = (cursor[0] + 1, cursor[1])
        f.write("#" if p != (0,0) else "S")
        cursor = (cursor[0] + 1, cursor[1])
    f.write("...\n")
    f.close()

iterations = 9
res = set(functools.reduce(lambda prev_node, current_node: functools.reduce(lambda old, new: old + [(i[0], i[1]) for i in itertools.zip_longest(range(old[-1][0], new[0], int(math.copysign(1, new[0] - old[-1][0]))), range(old[-1][1], new[1], int(math.copysign(1, new[1] - old[-1][1]))), fillvalue=(new[0] if abs(new[1] - old[-1][1]) > abs(new[0] - old[-1][0]) else new[1]))], prev_node, [(0,0)]), range(0,iterations), list(itertools.accumulate(open("9.input").readlines(), lambda head_tail, move: (head_tail[0] + (int(move[2:]) if move[0] in "RL" else 0) * (1 if move[0] == "R" else -1), head_tail[1] + (int(move[2:]) if move[0] in "UD" else 0) * (1 if move[0] == "D" else -1)), initial=(0,0)))))
visualize(res)
print(len(res))


THAT WAS F*ING PAIN
"""
import functools, math, itertools
print(len(set(functools.reduce(lambda prev_node, current_node: functools.reduce(lambda old, new: old + [(i[0], i[1]) for i in list(itertools.zip_longest(range(old[-1][0], new[0], int(math.copysign(1, new[0] - old[-1][0]))), range(old[-1][1], new[1], int(math.copysign(1, new[1] - old[-1][1]))), fillvalue=(new[0] if abs(new[1] - old[-1][1]) > abs(new[0] - old[-1][0]) else new[1])))[1:]], prev_node, [(0,0)]), range(0,9), list(itertools.accumulate(open("9.input").readlines(), lambda head_tail, move: (head_tail[0] + (int(move[2:]) if move[0] in "RL" else 0) * (1 if move[0] == "R" else -1), head_tail[1] + (int(move[2:]) if move[0] in "UD" else 0) * (1 if move[0] == "D" else -1)), initial=(0,0)))))))