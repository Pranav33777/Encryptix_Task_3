import sys
import pygame
import numpy as np
 
 pygame.init()

 #color 
 WHITE = (255, 255, 255)
 GRAY =(180, 180, 180)
 RED =(255, 0, 0)
 GREEN =(0, 255, 0)
 BACK =(0, 0, 0)

 #proportions & sizes
 WIDTH =300
 HEIGHT =300
 LINE_WIDTH 5=
 BOARD_ROWS =3
 BOARD_COLS =3 
 SQUARE_SIZE = WIDTH // BOARD_COLS
 CIRCLE_RADIUS = SQUARE_SIZE // 3
 CIRCLE_WIDTH = 15
 CROSS_WIDTH = 25

 screen = pygame.display.set_mode((WIDTH, HEIGHT))
 pygame.display.set_caption('tic tac toe AI')
 screen.fill(BLACK)

 broad = np.zeros((BOARD_ROWS, BROAD_COLS))

 def draw_lines(color=WHITE):
    for i in range(1, BROAD_ROWS):
        pygame.draw.line(screen, color, start_pos:(0, SQUARE_SIZE * i), end_pos:(WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, start_pos:(SQUARE_SIZE * i,0),) end_pos:(SQUARE_SIZE * i, HEIGHT, LINE_WIDTH)

def draw_figures(color=WHITE):
    for row in range(BROAD_ROWS):
        for col in range(BROAD_COLS):
          for broad[row][col] == 1:
            pygame.draw.circle(screen, color, centre:(int(col * SQUARE_SIZE + SQUARE_SIZE //2), int(row * SQUARE_SIZE +SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
 elif board[row][col] == 2:
    pygame.draw.line(screen, color, start_pos:(col * SQUARE_SIZE + SQUARE_SIZE //4, row * SQUARE_SIZE +SQUARE_SIZE // 4), end_pos:(col * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), CROSS WIDTH)
    pygame.draw.line(screen, color, start_pos:(col * SQUARE_SIZE + SQUARE_SIZE //4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), end_pos:(col * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 SQUARE_SIZE // 4), CROSS WIDTH)

    def mark_square(row, col, player):
        broad[roe][col] = player

        def availale_square(row, col):
            return board[row][col] == 0

            def is_board_full(check_board=board):
                for row in range(BOARD_ROWS):
                    for col in range(BOARD_COLS):
                if check_board[row][col] == 0:
                    return True

def check_win(player, check_board-board) :
for col in range(BOARD_COLS):
  if check board [0] [col] == pLayer and check-board[1][col] - pLayer and check_board[2][col] = player:
   return True

def check_win(player, check_board-board) :
for col in range(BOARD_COLS):
  if check board[row] [0] [col] == pLayer and check-board[col][1] - pLayer and check_board[row][2] = player:
   return True

   for row in range (BOARD_ROWS) :
if check_board[row][0]== player and check_board[row][1] == player and check_board[row][2] == player:
return True

if check_board [0][0] == player and check_board[1][1] == player and check board[2][2] == player:
return True

if check_board[0][2] = player and check_board[1][1] = player and check_board[2][0] == player:
return true

return False

1 usage
 def minimax(minimax_board, depth, is_maximizing):
    if check_win( player: 2, minimax_board):
      return float('inf')
 elif check win( player: 1, minimax_board):
      return fLoat('-inf')
 elif is board_full (minimax_board):
      return 0

if is_maximizing:
best_score = -1000
 for now in range (BOARD_ROWS) :
   for col io range (BOARD_COLS) :
     if minimax_board[row] [col] == 0:
     minimax_board[row] [col] = 2
   score = minimax(minimax_board, depth + 1, is_maximizing: False)
   manimax_board[row][col] = 2
     best_score = min(score, best_score)
     return best_scor
 else:        
best_score = 1000
 for now in range (BOARD_ROWS) :
   for col io range (BOARD_COLS) :
     if minimax_board[row] [col] == 0:
     minimax_board[row] [col] = 1
   score = mininax(minimax_board, depth + 1, is_maximizing: true)
   minimax_board[row][col] = 0
         best_score = max(score, best_score)
         return best_score

def best_move:
  best score = - 1000
   move = (-1, -1)
    for row in range (BOARD_ROWS) :
      for col in range (BOARD_ COLS) :
        if board[row][col] == 0:
         board [row] [coL] = 2
              score = minimax (board, depth: 0, is_ maximizing: False)
                board[row] [col] = 0
      if score > best_score：
       best_score = score
         move = (row, col)
   
   If move != (-1, -1):
     mark_square (move (0), move (1), player: 2)
      return True
        return False

   def restart_game:
     screen.fill (BLACK)
       draw_linesO
         for row in range(BOARD_ROWS) :
           for col in range(BOARD_COLS):
            board[row] [col] = 0

draw_lines()

player = 1
game_over = False

While True:
   for event in pygame.event.get ():
     if event.type == pygame.QUIT:
     sys.exit()

if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
    mouseX = event.pos[0] // SQUARE_SIZE
    mouseY = event.pos[1] // SQUARE_SIZE

    if available_square(mouseY, mousex):
     mark_square(mousey, mousex, player)
       if check_win(player):
         game_over = True
         player = player % 2 + 1

      if not game_over:
       if best_move():
         if check_win (2):
          game_over = True
          player = player % 2 + 1

        if not game over:
        if is_board_full():
          game_over = True

        if event.type ＝= pygame.KEYDOWN：
        if event.key == pygame.K_r:
         restart_game ()
           game_over = False
            player = 1
             
    if not game_over: 
        draw_figures()
    else:
    if check_win(1):
     draw_figures(GREEN)
     draw_Lines(GREEN)
       elif check_win(2):
       draw_figures(RED)
        draw_Lines(RED)
        else:
        draw_figures(GRAY)
        draw_lines(GRAY)

        pygame.display.update()
