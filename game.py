from tetris import Tetris
import pygame


def grid(game: Tetris, surface) -> None:

    for i in range(game.rows):
        for j in range(game.cols):
            pygame.draw.rect(surface, (100,100,100), (20*j,20*i,19,19), 1)
            if game.grid[i][j] > 0:
                pygame.draw.rect(surface, (120,120,120), (20*j,20*i,18,18))

    pygame.display.update()

def main():
    #### INITIALIZE PYGAME ####
    game = Tetris(300, 600)
    pygame.init()
    screen = pygame.display.set_mode((game.width, game.height))
    running = True
    #### SET TITLE AND ICONE ####
    pygame.display.set_caption("TETRIS")
    icon = pygame.image.load('src/tetris.png')
    pygame.display.set_icon(icon)
    #### SET UP A CLOCK #####
    clock = pygame.time.Clock()
    #### THE WHILE LOOP FOR THE GAME TO RUN ####
    while running:
        
        ### SET THE COLOR OF THE BACKGROUND TO WHITE ###
        screen.fill((255,255,255))
        grid(game,screen)
        game.draw_figure(screen)

        #### QUIT CONDITION ####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.go_left()
                if event.key == pygame.K_RIGHT:
                    game.go_right()
                if event.key == pygame.K_DOWN:
                    game.go_down()
                if event.key == pygame.K_UP and game.frozen == False:
                    game.figure.rotate()

        game.go_down()

        if game.state == "game over!":
            running = False
        #### UPDATE THE SCREEN AT THE END OF EACH LOOP ####
        clock.tick(10)
        pygame.display.update()

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 45, True, False)
    text = font.render("Score: " + str(game.score), True, (255,255,255))
    text_game_over = font1.render("Game Over", True, (255, 125, 0))

    is_over = True
    while is_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_over = False

        screen.fill((0,0,0))
        screen.blit(text, [20, 300])
        screen.blit(text_game_over, [20, 200])

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
