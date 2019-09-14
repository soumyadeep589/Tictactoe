import pygame
# from pygame.locals import *

x1 = "X"
grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

winner = None


def initBoard(display_var):
    background = pygame.Surface(display_var.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    pygame.draw.line(background, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(background, (0, 0, 0), (200, 0), (200, 300), 2)
    pygame.draw.line(background, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(background, (0, 0, 0), (0, 200), (300, 200), 2)

    return background


def drawStatus(board):
    global x1, winner
    if(winner is None):
        message = x1 + "'s turn"
    else:
        message = winner + " won!"

    image1 = pygame.image.load('refresh.png').convert_alpha()
    image2 = pygame.transform.scale(image1, (30, 30))
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))
    board.fill((250, 250, 250), (0, 300, 300, 25))
    board.blit(text, (10, 300))
    board.blit(image2, (260, 300))


def showBoard(display_var, board):
    drawStatus(board)
    display_var.blit(board, (0, 0))
    pygame.display.flip()


def refreshPage():
    global x1, winner, grid, board, display_var
    x1 = "X"
    grid = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    winner = None
    display_var = pygame.display.set_mode((300, 340))
    board = initBoard(display_var)


def boardPos(mouse_x, mouse_y):
    if mouse_y < 300:
        if(mouse_y < 100):
            row = 0
        elif(mouse_y < 200):
            row = 1
        else:
            row = 2

        if(mouse_x < 100):
            col = 0
        elif(mouse_x < 200):
            col = 1
        else:
            col = 2

        return (row, col)
    else:
        if mouse_x > 260:
            return 'refresh the page'
        else:
            return 'nothing to do'


def drawMove(board, board_row, board_col, piece):
    center_x = ((board_col)*100) + 50
    center_y = ((board_row)*100) + 50

    if(piece == 'O'):
        pygame.draw.circle(board, (0, 0, 0), (center_x, center_y), 44, 2)
    else:
        pygame.draw.line(board, (0, 0, 0), (center_x - 22, center_y - 22), (center_x + 22, center_y + 22), 2)
        pygame.draw.line(board, (0, 0, 0), (center_x + 22, center_y - 22), (center_x - 22, center_y + 22), 2)
    grid[board_row][board_col] = piece


def clickBoard(board):
    global grid, x1
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    data = boardPos(mouse_x, mouse_y)
    if data == 'nothing to do':
        return
    elif data == 'refresh the page':
        refreshPage()
    else:
        row, col = data
        if((grid[row][col] == "X") or (grid[row][col] == "O")):
            return

        drawMove(board, row, col, x1)

        if(x1 == "X"):
            x1 = "O"
        else:
            x1 = "X"

    # (row, col) = refreshPos(mouse_x, mouse_y)


def gameWon(board):
    global grid, winner

    for row in range(0, 3):
        if((grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] is not None)):
            winner = grid[row][0]
            pygame.draw.line(board, (250, 0, 0), (0, (row+1)*100 - 50), (300, (row + 1)*100 - 50), 2)
            break

    for col in range(0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
           (grid[0][col] is not None):
            winner = grid[0][col]
            pygame.draw.line(board, (250, 0, 0), ((col+1)*100 - 50, 0), ((col+1)*100 - 50, 300), 2)
            break
    if(grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
        winner = grid[0][0]
        pygame.draw.line(board, (250, 0, 0), (50, 50), (250, 250), 2)
    if(grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
        winner = grid[0][2]
        pygame.draw.line(board, (250, 0, 0), (250, 50), (50, 250), 2)


pygame.init()

display_var = pygame.display.set_mode((300, 340))
pygame.display.set_caption('Tic-Tac_Toe')

board = initBoard(display_var)

run = True

while(run):
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type is pygame.MOUSEBUTTONDOWN:
            clickBoard(board)
        gameWon(board)

        showBoard(display_var, board)

pygame.quit()
