import time
import random
dices=[1,2,3,4,5,6]
print("WELCOME TO SNAKE AND LADDERS")
n=int(input("Press 1 to play:Press 2 to exit:"))
if n==1:
    m=int(input(" press 1:to start"))
    user_score = 0
    computer_score=0
    if m==1:
        while True:
           if (user_score<100 and computer_score<100):
                user_choice=random.choice(dices)
                print("YOU GOT", user_choice, "ON THE DICE")
                computer_choice=random.choice(dices)
                print("COMPUTER GOT", computer_choice, "ON THE DICE")
                user_score = user_score + user_choice
                computer_score = computer_score + computer_choice
                if (user_score == 50):
                    user_score = user_score - 10
                    print("THE SNAKE ATE U STUPID")
                if (computer_score == 50):
                    computer_score = computer_score - 10
                    print("THE SNAKE ATE THE COMPUTER HAHA")
                if (user_score == 23):
                    user_score = user_score - 4
                    print("THE SNAKE ATE U STUPID")
                if (computer_score == 23):
                    computer_score = computer_score - 4
                    print("THE SNAKE ATE THE COMPUTER HAHA")
                if (user_score == 77):
                    user_score = user_score - 15
                    print("THE SNAKE ATE U STUPID")
                if (computer_score == 77):
                    computer_score = computer_score - 15
                    print("THE SNAKE ATE THE COMPUTER HAHA")
                if (user_score == 91):
                    user_score = user_score - 3
                    print("THE SNAKE ATE U STUPID")
                if (computer_score == 91):
                    computer_score = computer_score - 3
                    print("THE SNAKE ATE THE COMPUTER HAHA")
                if (user_score ==10):
                    user_score = user_score + 15
                    print("YAS! YOU GOT A LADDER")
                if (computer_score == 10):
                    computer_score = computer_score + 15
                    print("COMPUTER GOT A LADDER LUCKILY")
                if (user_score ==60):
                    user_score = user_score + 3
                    print("YAS! YOU GOT A LADDER")
                if (computer_score == 91):
                    computer_score = computer_score+ 3
                    print("COMPUTER GOT A LADDER LUCKILY")

                #time.sleep(1)
           if user_score>100:
               user_score-=user_choice
           if computer_score>100:
              computer_score-=computer_choice
           print("YOUR SCORE IS", user_score)
           print("COMPUTER SCORE IS", computer_score)
           print("\n")
           if (user_score==100):
               print(" CONGRATULATIONS YOU ARE THE WINNER")
               break
           if (computer_score==100):
               print(" HARD LUCK! COMPUTER IS THE WINNER")
               break
if n==2:
    print("GAME OVER")


