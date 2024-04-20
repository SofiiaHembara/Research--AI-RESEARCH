#level 8 code, performed by the GPT chat, all tests passed the first time
 
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    
#level 8 code, performed by Gemini chat, all tests passed the first time
def rps(p1, p2):
  """
  This function takes two arguments, p1 and p2, which represent the choices of player 1 and player 2 
  in a game of Rock-Paper-Scissors. It returns a string that declares the winner of the game.

  Args:
      p1 (str): The choice of player 1 (rock, paper, or scissors).
      p2 (str): The choice of player 2 (rock, paper, or scissors).

  Returns:
      str: A string that declares the winner of the game.
  """
  # Create a dictionary to map the choices to their winning counterparts
  beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

  # If the players choose the same option, it's a draw
  if p1 == p2:
    return "Draw!"
  # If player 1's choice beats player 2's choice, player 1 wins
  elif beats[p1] == p2:
    return "Player 1 won!"
  # Otherwise, player 2 wins
  else:
    return "Player 2 won!"

# Examples
print(rps("scissors", "paper")) # Output: Player 1 won!
print(rps("scissors", "rock")) # Output: Player 2 won!
print(rps("paper", "paper")) # Output: Draw!