sticks = 21

while sticks > 0:
    print("\nSticks left:", sticks)

    player = int(input("Pick 1 to 4 sticks: "))

    if player < 1 or player > 4 or player > sticks:
        print("Invalid choice!")
        continue

    sticks -= player

    if sticks == 0:
        print("You picked the last stick. You lose!")
        break

    computer = min(5 - player, sticks)
    print("Computer picked:", computer)

    sticks -= computer

    if sticks == 0:
        print("Computer picked the last stick. Computer loses!")
        print("You win!")
        break
