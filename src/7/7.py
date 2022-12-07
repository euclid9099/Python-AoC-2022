import functools
"""
f = open("7.input").read().split("$ ")[2:]

path = ["~"]
sizes = {}
for command in f:
    if command.startswith("cd"):
        if command.endswith("..\n"):
            path = path[:-1]
        else:
            path = path + [command.split()[1]]
        print(path)
    else:
        sizes.update({"/".join(path): list(map(lambda a: "/".join(path) + "/" + a.split()[1] if a.startswith("dir") else int(a.split()[0]), command.splitlines()[1:]))})
        #sizes["/".join(path)] = list(map(lambda a: "/".join(path) + "/" + a.split()[1] if a.startswith("dir") else int(a.split()[0]), command.splitlines()[1:]))

print(path)
print(sizes)
for elem in reversed(sizes):
    sizes[elem] = sum([i if type(i) is int else sizes[i] for i in sizes[elem]])

#print({"a": 1, "b": 2} | {"c": 3, "a": 65})
print(sum([sizes[i] for i in sizes if sizes[i] < 100000]))
#sizes.update({["/".join(path)]: list(map(lambda a: "/".join(path) + "/" + a.split()[1] if a.startswith("dir") else int(a.split()[0]), command.splitlines()[1:]))})
"""
print(sum(i for i in list(map(lambda listing: functools.reduce(lambda cur_listing, val: cur_listing | {val: sum(n if type(n) is int else cur_listing[n] for n in cur_listing[val])}, listing, listing), [functools.reduce(lambda path_sizes, command: (path_sizes[0][:-1] if command.endswith("..\n") else path_sizes[0] + [command.split()[1]], path_sizes[1]) if command.startswith("cd") else (path_sizes[0], {"/".join(path_sizes[0]): list(map(lambda a: "/".join(path_sizes[0]) + "/" + a.split()[1] if a.startswith("dir") else int(a.split()[0]), command.splitlines()[1:]))} | path_sizes[1] ), open("7.input").read().split("$ ")[2:], (["~"], dict()))[1]]))[0].values() if i < 100000))