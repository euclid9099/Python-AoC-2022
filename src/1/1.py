print(max(map(lambda block: sum(map(lambda number: int(number), block.split("\n"))),open('1.input', 'r').read().split('\n\n'))))
"""
Explanation:
                                                                                    open("1.input", "r").read()---------------------first, get entire content off file
                                                                                                               .split('\n\n')-------split it on every double newline to get an array of 'blocks'
          map(lambda block:                                                        ,                                         )------replace every block with a new field given back by the inner function
                            sum(map(lambda number: int(number), block.split("\n")))-------------------------------------------------split every block into its internal lines, replace them with their number representation
      max(                                                                                                                    )-----return the highest value
print(                                                                                                                         )----print the result to console
"""