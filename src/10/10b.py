import functools
print("\n".join("".join(["#" if abs(ele[0] - ele[1]) < 2 else " " for ele in enumerate(row)]) for row in list(map(lambda cpu: [cpu[i+0:i+40] for i in range(0,len(cpu),40)],[functools.reduce(lambda cycles_carry, command: (cycles_carry[0] + [cycles_carry[1]] * (1 if command[0] == "n" else 2), cycles_carry[1] + (0 if command[0] == "n" else int(command.split()[1]))), open("10.input", "r").readlines(), ([], 1))[0]]))[0]))