import pygame,random
pygame.init()

# create a function where you can initialize the program start values

#creates the frame 
(width,height) = (600,600)
# make the game board 30,30 boxes (600/30 = 20)
screen = pygame.display.set_mode((width,height))

pygame.display.flip()#no idea what this line does

clock = pygame.time.Clock() #timer for pygame it gets the last time the function was called

pygame.display.set_caption('Snake Game')#sets title for the window
#var for the of the snake
speedX = 0
speedY = 0
#position of the snake
Snake = [[60,20],[40,20],[20,20]]
dead = False
# position of the apple
apple = [60,60]
#colors
Blue = (0,0,255)
Red = (255,0,0)
White = (255,255,255)
Black = (0,0,0)
BoxSize = 20

#score
score = 0
#text
font = pygame.font.SysFont('arial',32)

#(game loop)code below keeps the window open unil the user presses x
running = True
while running:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(White)
#game code
    
    #keyboard input
    KeyEvent = pygame.key.get_pressed()
    #checks to see if the arrow keys were pressed
    if KeyEvent[pygame.K_LEFT]:
        speedY =0
        speedX =-BoxSize
    elif KeyEvent[pygame.K_RIGHT]:
        speedY = 0
        speedX =BoxSize
    elif KeyEvent[pygame.K_UP]:
        speedX = 0
        speedY =-BoxSize
    elif KeyEvent[pygame.K_DOWN]:
        speedX = 0
        speedY =BoxSize
    elif KeyEvent[pygame.K_r]:
            dead = False
            score = 0

    
    #if the snake is dead reset and tell the user their score
    if dead: 
        text = font.render('Press r to play again. Score:  '+str(score),True,Black,White)
        textrect = text.get_rect()
        textrect.center = (width//2,height//2)
        screen.blit(text, textrect) 
        pygame.display.update()  
        Snake = [[60,20],[40,20],[20,20]] 
        pygame.time.delay(100)  
        speedX = 0
        speedY = 0 
        
    #if the snake is not dead
    else: 
   # shifts the positon of the snake body  
        for i in range(len(Snake)-1,0,-1):
            if speedX!=0 or speedY!=0: 
                Snake[i][0] = Snake[i-1][0]
                Snake[i][1] = Snake[i-1][1]
            
        # increases the positon of the snake
        Snake[0][0] += speedX
        Snake[0][1] += speedY
           
        #checks to see if the snake is over the apple
        if Snake[0][0] == apple[0] and Snake[0][1] == apple[1]:
            apple[0] = random.randint(1,29)
            apple[1] = random.randint(1,29) 
            apple[0] *=BoxSize
            apple[1] *=BoxSize 
            Snake.append([-20,-20]) 
            score += 1

        #checks to see if the head runs over the body
        for x in range(0,len(Snake)):
            for y in range(0,len(Snake)):
                if (Snake[x][0] == Snake[y][0] and x!=y) and (Snake[x][1] == Snake[y][1] and x!=y): dead = True #checks to see if the snake has left the play area
        if Snake[0][0]>=BoxSize*30 or Snake[0][0]<=-BoxSize or Snake[0][1]>=BoxSize*30 or Snake[0][1]<=-BoxSize:
            dead = True
        
        #prints the snake 
        for i in range(0,len(Snake)):
            pygame.draw.rect(screen,Blue,(Snake[i][0],Snake[i][1],BoxSize,BoxSize))
             
        # draws the apple
        pygame.draw.rect(screen,Red,(apple[0],apple[1],BoxSize,BoxSize))

    pygame.display.update()# updates the entire screen  
            
    clock.tick(10) #T frames/second it will on (pauses the program until the correct time
