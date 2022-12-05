print(len([ranges for ranges in map(lambda line: list(map(lambda n: int(n), line.replace("-", ",").split(","))), open("4.input").read().splitlines()) if (ranges[0] >= ranges[2] and ranges[0] <= ranges[3]) or (ranges[0] <= ranges[2] and ranges[1] >= ranges[2])]))
"""
explanation:
                                                 list(map(lambda n: int(n), line.replace("-", ",").split(",")))     # turn each line into a list with 4 elements
                                map(lambda line:                                                               , open("4.input").read().splitlines())       # return a list of lists with each line from the file changed
          [ranges for ranges in                                                                                                                       if (ranges[0] >= ranges[2] and ranges[1] <= ranges[3]) or (ranges[0] <= ranges[2] and ranges[1] >= ranges[3])]        # returns a list where ranges overlap
print(len(                                                                                                                                                                                                                                                          ))      # prints the amount of lines for which a condition is true
"""