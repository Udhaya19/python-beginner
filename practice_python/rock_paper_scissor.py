def rock_paper_scissor():
    user1 = str(input("Enter the string:"))
    user2 = str(input("Enter the string:"))
    if user1 == user2:
        print("Game Tie")
        play_game = str(input("Play new game??(yes/no)"))
    elif ((user1 == "rock" and user2 == "scissor") or (user1 == "scissor" and user2 == "paper") or (
            user1 == "paper" and user2 == "rock")):

        print("user1 win!!! user2 loss")
        play_game = str(input("Play new game??(yes/no)"))

    else:
        print("user2 win!!! user1 loss")
        play_game = str(input("Play new game??(yes/no)"))
    if play_game == 'yes':
        print("The new game:")
        rock_paper_scissor()

    else:
        print("Game over")



rock_paper_scissor()
