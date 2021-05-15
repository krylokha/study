import random

person1_in_game = True
person2_in_game = True
result_person1 = 0
result_person2 = 0
turn = 1

def players_throw (sum):
    value = random.randint(2, 12)
    print('The current value is: ', value, ' ', value + sum)
    return(value)

def failure (result, person, step):
    if step%2 == 1:
        step = 1
    else:
        step = 2
    if result > 21:
        person = False
        break
    return('Player number ', step, ' is the winner')

while (person1_in_game) or (person2_in_game):
    if person1_in_game and turn%2 == 1:
        step1 = int(input('Its persons1 turn! Choose the command: ')) #whose turn
        if step1 == 1:
            #value1 = random.randint(2, 12) #peron's roll
            result_person1 = result_person1 + players_throw(result_person1)
            #if result_person1 > 21:
                #person1_in_game = False
                #print('Player number 2 is the winner')
                #break    
            failure(result_person1, person1_in_game, turn)
        if step1 == 2:
            person1_in_game = False #stop
            print('Pesron 1 is not in the game. The result of person 1 is ', result_person1)

    elif person2_in_game and turn%2 == 0:
        step2 = int(input('Its persons2 turn! Choose the command: '))
        if step2 == 1:
            #value2 = random.randint(2, 12)
            result_person2 = person2_in_game + players_throw(result_person2)
        if step2 == 2:
            person2_in_game = False
            print('Pesron 2 is not in the game. The result of person 2 is ', result_person2)
        if result_person2 > 21:
            person2_in_game = False
            print('Player number 1 is the winner')
            break
    f += 1

if person1_in_game and person2_in_game:
    if result_person1 > result_person2:
        print('Player number 1 is the winner')
    elif result_person1 < result_person2:
        print('Player number 2 is the winner')
    else:
        print('Draw')