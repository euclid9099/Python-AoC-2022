print(sum(map(lambda game: ((((ord(game.split(" ")[1]) - 86) % 3 - ord(game.split(" ")[0]) - 65)) % 3) * 3 + ord(game.split(" ")[1]) - 87, open("2.input", "r").read().splitlines())))
"""
Explanation:
                                                                                                                                           open("1.input", "r").read()      # first, get entire content off file
                                                                                                                                                                      .splitlines()     # split it on every newline to get an array of all games
          map(lambda game:                                                                                                               ,                                         )        # replace every block with a new field given back by the inner function
                               ord(game.split(" ")[1]) - 86        ord(game.split(" ")[0]) - 65              ord(game.split(" ")[1]) - 87       # turn A, B, C, X, Y, and Z into number 0 - 2
                           ((((                            ) % 3 -                             )) % 3) * 3 +        # reward points. The first part rewards points for winning (difference between own and other play), the second for the play itself (3x move number)
print(sum(                                                                                                                                                                          ))      # calculate sum of all games and print them to console
"""