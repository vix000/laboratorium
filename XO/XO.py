# Gra typu 'kółko i krzyżyk' - użytkownik gra przeciwko logice zaimplementowanej w programie
# Decyzje komputera są uwarunkowane kombinacjami w grze dającymi zwycięstwo - to do nich komputer będzie dążył.
# Gracz ma możliwość wyboru czy będzie zaczynał grę.
# Przy użyciu wielkich liter zadeklarowane są stałe.
# Bartłomiej Pysiak
# ---------------------------------------------------------------
# Using globals - I have to find a better way!
X = "X"
O = "O"
EMPTY_POSITION = ''
TIE = "It's the Tie!"

def display_rules():
  print(
    """
    Welcome in Tic-Tac-Toe game. Classic rules. Defeat the computer.
    The board will look like this:
    
    6 | 7 | 8
    ---------
    3 | 4 | 5
    ---------
    0 | 1 | 2
    
    """
    )

def choose_number(question):
  response = None
  while response not in range(0,10):
    try:
      response = int(input("Input a number from 0 to 8"))
    except:
      continue
    return response

def yes_or_no():
  """Function takes the question argument and returns either "y" string or "n" string"""
  answer = None
  while True:
    if answer not in ("y", "n"):
      answer = input("Answer [Y]es or [N]o: ").lower()
    else:
      break
  return answer

def who_goes_first():
  print("Player - do you want the first move?")
  while True:
    go_first = yes_or_no()
    if go_first == "y":
      player = X
      computer = O
      print("Player has the first move.")
    else:
      player = O
      computer = X
      print("Computer has the first move.")
    return player, computer

def display_board(the_board):
  print("\n\t", the_board[6], " | ", the_board[7], " | ", the_board[8], " ")
  print("\n\t", the_board[3], " | ", the_board[4], " | ", the_board[5], " ")
  print("\n\t", the_board[0], " | ", the_board[1], " | ", the_board[2], " ")
  
def new_board():
  the_board = []
  for i in range(9):
    the_board.append(EMPTY_POSITION)
  return the_board
  
def avaiable_positions(the_board):
  av_positions = []   # this list wil contain empty indexes of the_board list
  for position in range(9): # loop over every element of the board
    if the_board[position] == EMPTY_POSITION: # if any element of the board is empty:
      av_positions.append(position) # append it to the list
  return av_positions
  
def win_condition(the_board):
  """Important function! This is how program decides who won the game.
     If any of tuples in WIN_POSITIONS matches the positions of X's or O's on the board - it means that X or O won the game. If there is no EMPTY_POSITION and there is no match in if statement - its the tie. If none of this happens the game is still open."""
  WIN_POSITIONS = ((6,7,8),
                   (3,4,5),
                   (0,1,2),
                   (6,3,0),
                   (7,4,1),
                   (8,5,2),
                   (6,4,2),
                   (0,4,8))
  for i in WIN_POSITIONS:
    if the_board[i[0]] == the_board[i[1]] == the_board[i[2]] != EMPTY_POSITION:
      the_winner = the_board[i[0]] #it doesn't matter what position i return: all are either X's or O's
      return the_winner
    if EMPTY_POSITION not in the_board:
      return TIE
  return None
    
def player_turn(the_board, player):
  the_move = None
  while the_move not in avaiable_positions(the_board):
    the_move = choose_number("Choose a number")
    if the_move not in avaiable_positions(the_board):
      print("Try again")
  return the_move
  
def computer_turn(the_board, player, computer):
  board_copy = the_board[:]
  TACTICAL_POSITIONS = (4,6,2,6,8,1,3,5,7)
  for i in avaiable_positions(board_copy):
    board_copy[i] = computer
    if win_condition(board_copy) == computer:
      print(i)
      return i
    board_copy[i] = EMPTY_POSITION
    
  for i in avaiable_positions(board_copy):
    board_copy[i] = player
    if win_condition(board_copy) == player:
      print(i)
      return i
    board_copy[i] = EMPTY_POSITION
    
  for i in TACTICAL_POSITIONS:
    if i in avaiable_positions(the_board):
      print("Computer move:", i)
      return i

def pass_turn(the_turn):
  if the_turn == X:
    return O
  else:
    return X
    
def end_game(the_winner, player, computer):
  if the_winner != TIE:
    print(the_winner, " wins!")
  else:
    print(TIE)

def main():
  display_rules()
  player, computer = who_goes_first()
  the_turn = X
  the_board = new_board()
  
  while not win_condition(the_board):
    if the_turn == player:
      the_move = player_turn(the_board, player)
      the_board[the_move] = player
    else:
      the_move = computer_turn(the_board, player, computer)
      the_board[the_move] = computer
    display_board(the_board)
    the_turn = pass_turn(the_turn)
    
  the_winner = win_condition(the_board)
  end_game(the_winner, player, computer)

main()
