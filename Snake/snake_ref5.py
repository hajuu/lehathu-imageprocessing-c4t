# snake game
# by Roshan Kadu

# essential game imports
import pygame, sys, random, time

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, existing...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))  # setting display size
pygame.display.set_caption('==> Snake Game <==')
# time.sleep(5) #screen will sleep for 5 seconds

# Play background music
# pygame.mixer.music.load("nhacnen.mp3")
# pygame.mixer.music.get_volume()
# pygame.mixer.music.play(-1)

# colours
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# frames per second controller
fpsController = pygame.time.Clock()

# important variables
snakePos = [200, 300]  # it works like x and y axis [x,y]
snakeBody = [[200, 300], [1, 1], [3, 4], [5, 5]]

foodPos = [random.randrange(1, 72) * 10,
           random.randrange(1, 46) * 10]  # food position, its also like placing coordinate randomly
foodSpawn = True

score = 0

direction = 'UP'
changeto = direction


# game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    # pygame.mixer.music.stop()
    # pygame.mixer.pre_init(44100, -16, 2, 4096)
    # pygame.mixer.music.load("die.mp3")
    # pygame.mixer.music.play()
    time.sleep(10)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, red)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)


# main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # cheking if type of event is equal to event present in pygame i.e. QUIT
            pygame.quit()  # exit pygame
            sys.exit()  # exit console
        elif event.type == pygame.KEYDOWN:  # if user hit an button of keyboard
            if event.key == pygame.K_RIGHT or event.key == ord('d'):  # and if that button would be right arrow key
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'DOWN'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # changing direction of the snake by incrementing and decrementing x and y coordinate
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] += 10
    if direction == 'DOWN':
        snakePos[1] -= 10

    # snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        # pygame.mixer.pre_init(44100, -16, 2, 4096)
        # pygame.mixer.music.load("an.mp3")
        # pygame.mixer.music.play()
        time.sleep(0)
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    # Background
    playSurface.fill(white)

    # Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, black,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown,
                     pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(10)