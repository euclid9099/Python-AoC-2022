import functools
print(list(map(lambda list: [list[i] for i in range(len(list)) if list[i] > list[-1] - 40_000_000],[sorted(list(map(lambda listing: functools.reduce(lambda cur_listing, val: cur_listing | {val: sum(n if type(n) is int else cur_listing[n] for n in cur_listing[val])}, listing, listing), [functools.reduce(lambda path_sizes, command: (path_sizes[0][:-1] if command.endswith("..\n") else path_sizes[0] + [command.split()[1]], path_sizes[1]) if command.startswith("cd") else (path_sizes[0], {"/".join(path_sizes[0]): list(map(lambda a: "/".join(path_sizes[0]) + "/" + a.split()[1] if a.startswith("dir") else int(a.split()[0]), command.splitlines()[1:]))} | path_sizes[1] ), open("7.input").read().split("$ ")[2:], (["~"], dict()))[1]]))[0].values())]))[0][0])