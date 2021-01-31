
times=True
print("Hello,user welcome to the rock paper scissors game!")
while(times):
  start=input("type YES to start the game: ")
  start=start.lower()
  if(start=="yes"):
    print("\n")
    print("Let's begin with the game")
    print("\n")
    choice=input("Enter your choice:(rock,paper or scissors)").lower()
    options=["rock","paper","scissors"]
    from random import randint
    computer=options[randint(0,2)]
    print("you have selected",choice)
    print("I have selected",computer)
    if(choice==computer):
        print("Its a tie!")
    elif(choice==options[0] and computer==options[1]):
        print("computer wins!")
    elif(choice==options[1] and computer==options[2]):
        print("computer wins!")
    elif(choice==options[0] and computer==options[2]):
        print("Player wins!")
    elif(choice==options[1] and computer==options[0]):
      print("Player wins!")
    elif(choice==options[2] and computer==options[1]):
        print("Player wins!")
    elif(choice==options[2] and computer==options[0]):
        print("Computer wins!")
    else:
        print("You have not entered the selected choices, please enter again")
  elif(start=="no"):
    print("Ok then,lets play afterwards!")
    times=False
