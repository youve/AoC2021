#!/bin/env python

import fileinput
from dataclasses import dataclass


@dataclass
class Player():
    name: str
    spot: int
    score: int = 0


@dataclass
class GameState():
    dice: list[int] = tuple(range(1, 101))
    dice_index: int = 0
    board: list[int] = (10, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    moves: int = 0
    won: bool = False


def parse(file):
    players = []
    for line in file:
        player, spot = line.split(" starting position: ")
        spot = int(spot)
        players.append(Player(player, spot))
    return players


def move_player(player, gameboard):
    i = gameboard.dice_index
    dice = gameboard.dice[i:i + 3]
    wrap_around = 3 - len(dice)
    dice += gameboard.dice[:wrap_around]

    new_position = (player.spot + sum(dice)) % 10  # index
    player.spot = gameboard.board[new_position]   # value
    player.score += player.spot
    gameboard.dice_index = dice[-1]
    gameboard.moves += 3

    if player.score >= 1000:
        gameboard.won = True

    return player, gameboard


players = parse(fileinput.input())
gameboard = GameState()

while not gameboard.won:
    for i, player in enumerate(players):
        players[i], gameboard = move_player(player, gameboard)
        if player.score >= 1000:
            break

print(gameboard.moves * min(player.score for player in players))
