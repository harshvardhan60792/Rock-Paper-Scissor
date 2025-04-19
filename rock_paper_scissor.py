import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("Welcome to Rock, Paper, Scissor Game")
print("Please choose one of the following: ")
print("1 for Rock")
print("2 for Paper")
print("3 for Scissor")
choice=int(input("Enter your choice : "))
computer=random.randint(1,3)
if choice==1:
    print("YOU CHOSE ROCK"+rock)
    if computer==1:
        print(f"Computer chose Rock.\n{rock}\nIt's a tie!")
    elif computer==2:
        print(f"Computer chose Paper.\n{paper}\nPaper covers Rock.\nYou lose")
    else:
        print(f"Computer chose Scissor.\n{scissor}\nRock smashes Scissor.\nYou win")
elif choice==2:
    print("YOU CHOSE PAPER"+paper)
    if computer==1:
        print(f"Computer chose Rock.\n{rock}\nPaper covers Rock.\nYou win")
    elif computer==2:
        print(f"Computer chose Paper.\n{paper}\nIt's a tie!")
    else:
        print(f"Computer chose Scissor.\n{scissor}\nScissor cuts Paper.\n You lose")
elif choice==3:
    print("YOU CHOSE SCISSOR"+scissor)
    if computer==1:
        print(f"Computer chose Rock.\n{rock}\nRock smashes Scissor.\nYou lose")
    elif computer==2:
        print(f"Computer chose Paper.\n{paper}\nScissor cuts Paper.\nYou win")
    else:
        print(f"Computer chose Scissor.\n{scissor}\nIt's a tie!")
else:
    print("Invalid choice.")
