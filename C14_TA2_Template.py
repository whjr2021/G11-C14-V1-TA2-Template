import pygame
import time

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

class Player:
    # Define the __init__ method with properties- self, name, xloc, yloc

    



        
    def image_load(self, location, width, height):
        img = pygame.image.load(location).convert_alpha()
        img_scaled = pygame.transform.smoothscale(img,(width,height))
        return img_scaled
    
    def player_name(self, position):
        font = pygame.font.Font(None, 30)
        text = font.render(self.name, 1, (0, 255,255))
        screen.blit(text, position)
        
    def text_display(size,text,r,g,b,x,y):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, (r,g,b))
        screen.blit(text, (x,y))

    def move_up(self):
        self.yloc -= 10
        return self.yloc
    
    def move_down(self):
        self.yloc += 10
        return self.yloc
    
    def move_left(self):
        if self.xloc >= 50:                          
            self.xloc -= 10 
        return self.xloc
    
    def move_right(self):
        if self.xloc <= 320:                          
            self.xloc += 10
        return self.xloc   

carx = 140
cary = 450
bgy = 0
counter = 0

# Create a player object of class Player
# 1. Create "player1" object of class Player with properties - "John", carx, cary


carryOn = True
t1 = time.time()

while carryOn:
    bgImg = pygame.image.load("road.png").convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    # Display the player1 car image and name
    # 1. Display yellow car scaled to (230, 140) 

    # 2. Display player1 name at location (carx+90, cary+130)

    
    # Update player location
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.KEYDOWN:
            # 1. Check for up arrow key press for player1


                bgy -= 10
            # 2. Check for down arrow key press for player1


                bgy += 10
            # 3. Check for right arrow key press for player1


            # 4. Check for left arrow key press for player1

    
    
    if cary <= 30:
        bgy = 0
        cary = 450
        counter += 1
            
    t2 = time.time()
    game_time = t2-t1
    game_time = round(game_time, 2)
    
    # Display game time elapsed
    Player.text_display(35,"TIME ELAPSED: " + str(game_time)+ "seconds",0, 255,255,130,15)
    
    # Display finish line after 5 iterations of game loop
    # Check if "counter" is equal to 5
    if counter == 5:
        # Create and draw the finish line white-colored rectangle at (x,y)=(95, 40) with width=400 and height=30
        finish_line = pygame.Rect(95,40,400,30)
        pygame.draw.rect(screen,(255,255,255),finish_line)
        Player.text_display(40, "----------FINISH----------", 255,0,0,160,45)
        pygame.display.flip()
        
        # End the game loop after displaying finish line
        pygame.time.wait(3000)
        screen.fill((0,100,200))        
        Player.text_display(40,"Finish time: " + str(round(game_time,2))+ " seconds",255,255,255,140,200)       
        Player.text_display(40,"Game Over, Good Luck Next Time!",255,255,255,80,250)       
        pygame.display.flip()
        pygame.time.wait(5000)
        # Break out of 'while' game loop
        break
    
    screen.blit(yellow_car, (carx, cary))

    pygame.display.flip()
pygame.quit()