from random import choice


def beat(pl, cmp, figures):
    positions = figures[::]
    while positions.index(pl) != len(positions) // 2:
        positions.append(positions.pop(0))
    return positions.index(pl) > positions.index(cmp)


name = input('Enter your name: ')
print('Hello,', name)
score = 0
options = input()
if options == '':
    options = ['rock', 'paper', 'scissors']
else:
    options = options.split(',')

with open('rating.txt', 'r') as file:
    for line in file:
        name_, score_ = line.split()
        if name_ == name:
            score = int(score_)

print("Okay, let's start")
while True:
    player_choice = input()
    if player_choice == '!exit':
        break
    if player_choice == '!rating':
        print('Your rating:', score)
        continue
    if player_choice not in options:
        print('Invalid input')
        continue
    comp_choice = choice(options)
    if player_choice == comp_choice:
        print(f'There is a draw ({comp_choice})')
        score += 50
    elif beat(player_choice, comp_choice, options):
        print(f'Well done. The computer chose {comp_choice} and failed')
        score += 100
    else:
        print(f'Sorry, but the computer chose {comp_choice}')

