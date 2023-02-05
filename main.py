import sys


class Player:
    name: str
    old: int
    score: int

    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


lst_in = list(map(str.strip, sys.stdin.readlines()))

players = [Player(*map(lambda x: int(x) if x.isdigit() else x, string.split('; '))) for string in lst_in]

players_filtered = list(filter(bool, players))
