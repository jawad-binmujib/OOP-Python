#6
import random
def playRockPaperScissor(rounds):
    count = 0
    count1 = 0
    for rou in range(rounds):
        player_action = input()
        option = ('rock' , 'paper','scissor')
        Computer = random.choice(option)
        print(Computer)
        if player_action == Computer:
            count+=1
            count1+=1
        elif player_action == 'rock' and Computer == 'paper':
            count1+= 1
        elif player_action == 'paper' and Computer == 'scissor':
            count1+=1
        elif player_action == 'scissor' and Computer == 'rock':
            count1+=1
        else:
            count+=1
    print(f"Your Score:{count}")
    print(f"Computer's Score:{count1}")
    if count > count1:
        print(f"You have won the game!")
    elif count == count1:
        print(f"It's a tie!")
    else:
        print(f"Computer has won the game!")
rounds = int(input())
playRockPaperScissor(rounds)
