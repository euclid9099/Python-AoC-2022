print(sum(map(lambda badge: badge - 96 if badge > 96 else badge - 38, map(lambda rucksacks: ord(set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2])).pop()), (open("3.input", "r").read().splitlines()[i:i+3] for i in range(0, len(open("3.input", "r").read().splitlines()), 3))))))
"""
Explanation:
                                                                                                                                                                                           open("3.input", "r").read().splitlines()     # read the entire file (as always)
                                                                                                                                                                                          (                                        [i:i+3] for i in range(0, len(open("3.input", "r").read().splitlines()), 3))     # group every three value by using a oneline for loop
                                                                      map(lambda rucksacks: ord(set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2])).pop()),                                                                                                                      )        # get the only element that is in every element per group
          map(lambda badge: badge - 96 if badge > 96 else badge - 38,                                                                                                                                                                                                                                           )       # replace the symbol with its priority
print(sum(                                                                                                                                                                                                                                                                                                       ))     # sum it all up and print the result
"""