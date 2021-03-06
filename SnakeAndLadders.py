import time
import random
import sys

sleepActions = 1
Goal = 100
diceFace = 6

snakes = {
    8: 4, 18: 1, 26: 10, 39: 5, 51: 6, 54: 36, 56: 1, 60: 23, 75: 28, 83: 45, 85: 59, 90: 48, 92: 25, 97: 87, 99: 63
}

ladders = {
    3: 20, 6: 14, 11: 28, 15: 34, 17: 74, 22: 37, 38: 59, 49: 67, 57: 76, 61: 78, 73: 86, 81: 98, 88: 91
}

turnText = ["Your Turn!"]
snakeBite = ["Pssst! Snake Bite!"]
ladderJump = ["Yayy!! A Ladder!"]


def welcomeScreen():
    msg = """
    Welcome to Snake and Ladder Game.

    Rules:
      1. Initially both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
    """
    print(msg)


def getPlayerName():
    player1Name = None
    while not player1Name:
        player1Name = input("Player 1 enter your name: ").strip().upper()

    player2Name = None
    while not player2Name:
        player2Name = input("Player 2 enter your name: ").strip().upper()

    print(f"Match will be played between {player1Name} and {player2Name}")
    return player1Name, player2Name


def getDiceValue():
    time.sleep(sleepActions)
    diceValue = random.randint(1, diceFace)
    print(f"Its a {str(diceValue)}")
    return diceValue


def gotSnakeBite(prevValue, currentValue, playerName):
    print(f"{random.choice(snakeBite).upper()} ~~~~~~~~C")
    print(f"{playerName} got a snake bite. Down from {str(prevValue)} to {str(currentValue)}")


def gotLadderJump(prevValue, currentValue, playerName):
    print(f"{random.choice(ladderJump).upper()} ########")
    print(f"{playerName} climbed the ladder from {str(prevValue)} to {str(currentValue)}")


def snakeLadder(playerName, currentValue, diceValue):
    time.sleep(sleepActions)
    prevValue = currentValue
    currentValue = currentValue + diceValue

    if currentValue > Goal:
        print(f"You need {str(Goal - prevValue)} to win this game. Keep trying.")
        return prevValue

    print(f"{playerName} moved from {str(prevValue)} to {str(currentValue)}")
    if currentValue in snakes:
        finalValue = snakes.get(currentValue)
        gotSnakeBite(currentValue, finalValue, playerName)

    elif currentValue in ladders:
        finalValue = ladders.get(currentValue)
        gotLadderJump(currentValue, finalValue, playerName)

    else:
        finalValue = currentValue

    return finalValue


def winStatus(playerName, position):
    time.sleep(sleepActions)
    if Goal == position:
        print(f"Thats it! {playerName} won the game.")
        print(f"Congratulations {playerName}")
        print("Thank you for playing the game.")
        sys.exit(1)


def start():
    welcomeScreen()
    time.sleep(sleepActions)
    player1Name, player2Name = getPlayerName()
    time.sleep(sleepActions)

    player1CurrentPosition = 0
    player2CurrentPosition = 0

    while True:
        time.sleep(sleepActions)
        firstInput = input(f"{player1Name}:{random.choice(turnText)} Hit the enter to roll dice: ")
        print("Rolling dice...")
        diceValue = getDiceValue()
        time.sleep(sleepActions)
        print(f"{player1Name} moving....")
        player1CurrentPosition = snakeLadder(player1Name, player1CurrentPosition, diceValue)

        winStatus(player1Name, player1CurrentPosition)


if __name__ == "__main__":
    start()
