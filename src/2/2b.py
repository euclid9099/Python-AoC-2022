print(sum(map(lambda elem: 3 * (ord(elem.split(" ")[1]) - 88) + ((ord(elem.split(" ")[0]) - 65) + (ord(elem.split(" ")[1]) - 88) - 1) % 3 + 1, open("2.input", "r").read().splitlines())))
"""
Explanation:
                                                                                                                                               open("1.input", "r").read()                  first, get entire content off file
                                                                                                                                                                          .splitlines()     split it on every newline to get an array of all games
          map(lambda game:                                                                                                                   ,                                         )    replace every block with a new field given back by the inner function
                                ord(game.split(" ")[1]) - 88      ord(game.split(" ")[0]) - 65     ord(game.split(" ")[1]) - 88                                                             turn A, B, C, X, Y, and Z into number 0 - 2
                           3 * (                            ) + ((                            ) + (                            ) - 1) % 3 + 1                                               first part: reward 3 * points for the win int + points for the move itself
print(sum(                                                                                                                                                                              ))  calculate sum of all games and print them to console
"""