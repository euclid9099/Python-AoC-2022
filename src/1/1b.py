print(sum(sorted(list(map(lambda block: sum(map(lambda number: int(number), block.split("\n"))),open("1.input", "r").read().split("\n\n"))))[-3:]))
"""
Explanation:
                                                                                                open("1.input", "r").read()-------------------------first, get entire content off file
                                                                                                                           .split('\n\n')-----------split it on every double newline to get an array of 'blocks'
                      map(lambda block:                                                        ,                                         )----------replace every block with a new field given back by the inner function
                                        sum(map(lambda number: int(number), block.split("\n")))-----------------------------------------------------split every block into its internal lines, replace them with their number representation
          sorted(list(                                                                                                                    ))--------turn the map object into a list and sort it
      sum(                                                                                                                                  [-3:])--get the last three elements of the sorted block array, and sum them up
print(                                                                                                                                            )-print the result to console
"""