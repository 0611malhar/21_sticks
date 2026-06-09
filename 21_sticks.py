sticks = 21

while sticks > 0:
    print("\nSticks left:", sticks)
    player = int(input("Pick 1 to 4 sticks: "))

    if player < 1 or player > 4:
        print("Invalid choice!")
        continue
    sticks -= player
    if sticks <= 0:
        print("You picked the last stick. You lose!")
        break
    computer = 5 - player
    print("Computer picked:", computer)
    sticks -= computer
    if sticks <= 0:
        print("Computer picked the last stick. Computer loses!")
        print("You win!")
        break
