#!/bin/env python3
import numpy as np

def open_file():
    with open('input', 'r') as f:
        balls = [int(x) for x in f.readline().strip().split(',')]
        cards = []
        new_card = []
        for _ in range(100):
            for i in range(0,6):
                line = f.readline().strip()
                if len(line) > 0:
                    line = [int(x) for x in line.split(' ') if x]
                    new_card.append(line)
            cards.append(new_card)
            new_card = []
    return balls, cards

def get_win(card, arr):
    ''' Returns position in arr at which this card would win
    It turns out diagonals don't count in this problem,
    but I've left the code there in case it changes in part 2.
    '''
    card = np.array(card)
    wins = {}
    wins['rows'] = [0, 0, 0, 0, 0]
    wins['cols'] = [0, 0, 0, 0, 0]
    #wins['diags'] = [0, 0]
    for i, ball in enumerate(arr):
        row, col = np.where(card == ball)
        if row.size != 0:
            wins['rows'][row[0]] += 1
            wins['cols'][col[0]] += 1
     #       if row[0] == col[0]:
     #           wins['diags'][0] += 1
     #       elif row[0] + col[0] == 4:
     #           wins['diags'][1] += 1
     #       if (wins['rows'][row[0]] == 5) or (wins['cols'][col[0]] == 5) or (wins['diags'][0] == 5) or (wins['diags'][1] == 5):
            if (wins['rows'][row[0]] == 5) or (wins['cols'][col[0]] == 5):
#                print(wins)
                return i
    return 999999

def get_uncalled_numbers(card, arr, ball_index):
    sum = 0
    for line in card:
        for num in line:
            if num not in arr[0:ball_index + 1]:
                sum += num
    return sum

balls, cards = open_file()

win_positions = [get_win(card, balls) for card in cards]
#print(win_positions)
winning_ball = min(win_positions)
winning_card = cards[win_positions.index(winning_ball)]

sum_uncalled = get_uncalled_numbers(winning_card, balls, winning_ball)

print("\nThe winning card is:")
for line in winning_card:
    print(line)
print(f'The balls called were: {balls[:winning_ball+1]}')
print(sum_uncalled*balls[winning_ball])

last_winning_ball = max(win_positions)
losing_card = cards[win_positions.index(last_winning_ball)]
sum_uncalled = get_uncalled_numbers(losing_card, balls, last_winning_ball)

print("\nAnd the loser is:")
for line in losing_card:
    print(line)
print(f'The balls called were: {balls[:last_winning_ball+1]}')
print(sum_uncalled*balls[last_winning_ball])
