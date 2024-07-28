import sys, menu
import pygame, random
from pygame.math import Vector2

pygame.init()
pygame.display.set_caption("Dragon")


class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(6,10), Vector2(5,10), Vector2(4,10)]
        self.direction = Vector2(0,1)
        self.new_block=False
        #self.new_block = False

        self.head_down = pygame.image.load("images/head_down.png").convert_alpha()
        self.head_left = pygame.image.load("images/head_left.png").convert_alpha()
        self.head_right = pygame.image.load("images/head_right.png").convert_alpha()
        self.head_up = pygame.image.load("images/head_up.png").convert_alpha()

        self.body_bl = pygame.image.load("images/body_bl.png").convert_alpha()
        self.body_br = pygame.image.load("images/body_br.png").convert_alpha()
        self.body_tl = pygame.image.load("images/body_tl.png").convert_alpha()
        self.body_tr = pygame.image.load("images/body_tr.png").convert_alpha()

        self.body_horizontal = pygame.image.load("images/body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load("images/body_vertical.png").convert_alpha()
        
        self.tail_down = pygame.image.load("images/tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("images/tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("images/tail_right.png").convert_alpha()
        self.tail_up = pygame.image.load("images/tail_up.png").convert_alpha()


    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
         
        for index, block in enumerate(self.body):
            #create a rectangle
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            #draw the rectangle
            if index == 0:
                screen.blit(self.head, block_rect )
            elif index == len(self.body)-1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block=self.body[index+1] - block
                next_block=self.body[index-1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x==-1 and next_block.y== 1 or previous_block.y== 1 and next_block.x==-1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x== 1 and next_block.y==-1 or previous_block.y==-1 and next_block.x== 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x== 1 and next_block.y== 1 or previous_block.y== 1 and next_block.x== 1:
                        screen.blit(self.body_br, block_rect)
            
    def update_head_graphics(self):
        head_relation=self.body[1]-self.body[0]
        if head_relation==Vector2(1,0):self.head=self.head_left
        elif head_relation==Vector2(-1,0):self.head=self.head_right
        elif head_relation==Vector2(0,-1):self.head=self.head_down
        elif head_relation==Vector2(0,1):self.head=self.head_up

    def update_tail_graphics(self):
        tail_relation=self.body[-2]-self.body[-1]
        if tail_relation==Vector2(1,0):self.tail=self.tail_left
        elif tail_relation==Vector2(-1,0):self.tail=self.tail_right
        elif tail_relation==Vector2(0,-1):self.tail=self.tail_down
        elif tail_relation==Vector2(0,1):self.tail=self.tail_up

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
    
    def reset(self):
        self.body = [Vector2(6,10), Vector2(5,10), Vector2(4,10)]

        self.direction = Vector2(0,1)

clock = pygame.time.Clock()

class Fruit:
    def __init__(self):
        self.pos = self.randomize()

    def draw_fruit(self):
        # Create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # Draw the fruit image onto the rectangle
        screen.blit(potion, fruit_rect)

    def randomize(self):
        # Generate random x and y coordinates within the grid
        x = random.randint(0, cell_number - 1)
        y = random.randint(0, cell_number - 1)
        return Vector2(x, y)


class MAIN:

    
    def __init__(self, multi:bool):
        if multi:
            self.snake = Snake()
            self.snake2= Snake()
            self.fruit = Fruit()
            self.snake2.body = [Vector2(15,10), Vector2(14,10), Vector2(13,10)]
            
            # Just nu startar den direkt
            # Ha if statement (om spelare 1 rör sig börjar draken röra sig, annars stilla)
            self.snake2.direction=Vector2(0,-1)
            self.snake2.head_down = pygame.image.load("images/ghead_down.png").convert_alpha()
            self.snake2.head_left = pygame.image.load("images/ghead_left.png").convert_alpha()
            self.snake2.head_right = pygame.image.load("images/ghead_right.png").convert_alpha()
            self.snake2.head_up = pygame.image.load("images/ghead_up.png").convert_alpha()

            self.snake2.body_bl = pygame.image.load("images/gbody_bl.png").convert_alpha()
            self.snake2.body_br = pygame.image.load("images/gbody_br.png").convert_alpha()
            self.snake2.body_tl = pygame.image.load("images/gbody_tl.png").convert_alpha()
            self.snake2.body_tr = pygame.image.load("images/gbody_tr.png").convert_alpha()

            self.snake2.body_horizontal = pygame.image.load("images/gbody_horizontal.png").convert_alpha()
            self.snake2.body_vertical = pygame.image.load("images/gbody_vertical.png").convert_alpha()
            
            self.snake2.tail_down = pygame.image.load("images/gtail_down.png").convert_alpha()
            self.snake2.tail_left = pygame.image.load("images/gtail_left.png").convert_alpha()
            self.snake2.tail_right = pygame.image.load("images/gtail_right.png").convert_alpha()
            self.snake2.tail_up = pygame.image.load("images/gtail_up.png").convert_alpha()
    

        else:
            self.snake = Snake()
            self.fruit = Fruit()

    def update(self, multi):
        if multi:
            self.snake.move_snake()
            self.snake2.move_snake()
            self.check_collision(True)
            self.winner(True)
        else:
            self.snake.move_snake() 
            self.check_collision(False)
            self.winner(False)
    
    def draw_elements(self, multi):
        if multi:
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.snake2.draw_snake()
            head_rect = pygame.Rect(int(self.snake.body[0].x * cell_size), int(self.snake.body[0].y * cell_size), cell_size, cell_size)
            head_rect2 = pygame.Rect(int(self.snake2.body[0].x * cell_size), int(self.snake2.body[0].y * cell_size), cell_size, cell_size)
            self.draw_score(True)
            #For snake1
            if self.snake.direction == (-1, 0):
                screen.blit(self.snake.head_left, head_rect)

            elif self.snake.direction == (1,0):
                screen.blit(self.snake.head_right, head_rect)

            elif self.snake.direction == (0,1):
                screen.blit(self.snake.head_down, head_rect)

            elif self.snake.direction == (0,-1):
                screen.blit(self.snake.head_up, head_rect)

            #For snake2
            if self.snake2.direction == (-1, 0):
                screen.blit(self.snake2.head_left, head_rect2)

            elif self.snake2.direction == (1,0):
                screen.blit(self.snake2.head_right, head_rect2)

            elif self.snake2.direction == (0,1):
                screen.blit(self.snake2.head_down, head_rect2)

            elif self.snake2.direction == (0,-1):
                screen.blit(self.snake2.head_up, head_rect2)
        
        else:
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            head_rect = pygame.Rect(int(self.snake.body[0].x * cell_size), int(self.snake.body[0].y * cell_size), cell_size, cell_size)
            self.draw_score(False)

            if self.snake.direction == (-1, 0):
                screen.blit(self.snake.head_left, head_rect)

            elif self.snake.direction == (1,0):
                screen.blit(self.snake.head_right, head_rect)

            elif self.snake.direction == (0,1):
                screen.blit(self.snake.head_down, head_rect)

            elif self.snake.direction == (0,-1):
                screen.blit(self.snake.head_up, head_rect)
            if self.fruit.pos == self.snake.body[0]:
                #reposition fruit
                self.fruit.randomize()
                #add another block to snake
                self.snake.add_block()
            
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()


    def check_collision(self, multi):
        if multi:
            if self.fruit.pos == self.snake.body[0]:
                #reposition fruit
                self.fruit.pos.x = random.randint(0, cell_number - 1)
                self.fruit.pos.y = random.randint(0, cell_number - 1)
                #add another block to snake
                self.snake.add_block()
            
            if self.fruit.pos == self.snake2.body[0]:
                #reposition fruit
                self.fruit.pos.x = random.randint(0, cell_number - 1)
                self.fruit.pos.y = random.randint(0, cell_number - 1)
                #add another block to snake
                self.snake2.add_block()

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.pos.x = random.randint(0, cell_number - 1)
                    self.fruit.pos.y = random.randint(0, cell_number - 1)
                
            
            for block in self.snake2.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.pos.x = random.randint(0, cell_number - 1)
                    self.fruit.pos.y = random.randint(0, cell_number - 1)
        
        else:
            if self.fruit.pos == self.snake.body[0]:
                #reposition fruit
                self.fruit.pos.x = random.randint(0, cell_number - 1)
                self.fruit.pos.y = random.randint(0, cell_number - 1)
                #add another block to snake
                self.snake.add_block()
            
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.pos.x = random.randint(0, cell_number - 1)
                    self.fruit.pos.y = random.randint(0, cell_number - 1)


                
    def game_over(self):
        global run
        run = True
        

    #function with logic that establishes and determins the winner based on different snake collision cases
    def winner(self,multi):
        global menu_title, run
        if multi:
            #check if snake is outside of screen
            if not 0 <= self.snake.body[0].x < cell_number or not 0<=self.snake.body[0].y <cell_number:
                run = True
                menu_title = "Green won"

            if not 0 <= self.snake2.body[0].x < cell_number or not 0<=self.snake2.body[0].y <cell_number:
                run = True
                menu_title = "Orange won"

            
            for block in self.snake.body[1:]:
                #check if snake1 hits itself
                if block == self.snake.body[0]:
                    menu_title = "Green won"
                    run = True

                #check if snake2 hits snake1s body
                if block == self.snake2.body[0]:
                    menu_title = "Orange won"
                    run = True


            #check if snake 2 hits itself
            for block2 in self.snake2.body [1:]:
                #check if snake2 hits itself
                if block2 == self.snake2.body[0]:
                    menu_title = "Orange won"
                    run = True

                #check if snake1 hits snake2s body
                if block2 == self.snake.body[0]:
                    menu_title = "Green won"
                    run = True
        
            #logic for head to head collision.            
            if self.snake.body[0]==self.snake2.body[0]:
                menu_title = "Draw"
                run = True
        
        else:
            #check if snake is outside of screen
            # Have seperate if staremnts for the differant snakes, due to differant wanted outcome. 
            if not 0 <= self.snake.body[0].x < cell_number or not 0<=self.snake.body[0].y <cell_number:
                points = len(self.snake.body)
                run = True
                menu_title = "You got "+ str(points-3) + " points!"
                self.snake.reset()
            
            for block in self.snake.body[1:]:
                #check if snake hits itself
                if block == self.snake.body[0]:
                    menu_title = "You got "+ str(len(self.snake.body)-3) + " points!"
                    run = True


    def draw_grass(self):
        grass_color = (187,57,219)

        for row in range(cell_number):
            if row % 2 == 0:
             for column in range(cell_number):
                if column %2 == 0:
                    grass_rect = pygame.Rect(column * cell_size, row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
    
    
    def draw_score(self,multi:bool):
        if multi:
            # For snake1
            score_text = str(len(self.snake.body) - 3)
            score_surface = game_font.render(score_text,True,pygame.Color("black"))
            score_x = int(110)
            score_y = int(cell_size*cell_number-40)
            
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            potion_rect = potion.get_rect(midright= (score_rect.left-35, score_rect.centery))

            screen.blit(score_surface, score_rect)
            screen.blit(self.snake.head_right, potion_rect)

            # For snake2
            score_text = str(len(self.snake2.body) - 3)
            score_surface = game_font.render(score_text,True,pygame.Color("black"))

            #Fix symetry of scoreboxes
            score_x = int(cell_size*cell_number-40)
            score_y = int(cell_size*cell_number-40)
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            potion_rect = potion.get_rect(midright= (score_rect.left-35, score_rect.centery))

            screen.blit(score_surface, score_rect)

            # Use the heads of the snakes/dragons instead of potioin to show score
            screen.blit(self.snake2.head_right, potion_rect)
            
        
        else:
            # For snake
            score_text = str(len(self.snake.body) - 3)
            score_surface = game_font.render(score_text,True,pygame.Color("black"))
            score_x = int(cell_size*cell_number-40)
            score_y = int(cell_size*cell_number-40)
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            potion_rect = potion.get_rect(midright= (score_rect.left-35, score_rect.centery))

            screen.blit(score_surface, score_rect)
            screen.blit(self.snake.head_right, potion_rect)


cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_number * cell_size))
potion = pygame.image.load("images/potion.png").convert_alpha()
game_font = pygame.font.Font("images/Chatlong.ttf", 25)
main_game = MAIN(True)
single_main_game = MAIN(False)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
mode = False
run = True
menu_title = "Dragon Menu"


while True:

    if run:
        mode = menu.main_menu(menu_title)
        run = False
        main_game.snake.reset()
        
        main_game.snake2.body = [Vector2(15,10), Vector2(14,10), Vector2(13,10)]
        main_game.snake2.direction = (0,-1)
        
    if mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == SCREEN_UPDATE:
                main_game.update(True)
                main_game.winner(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and main_game.snake.direction != (0,1):
                    main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_a and main_game.snake.direction != (1,0):
                    main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_d and main_game.snake.direction != (-1,0):
                    main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_s and main_game.snake.direction != (0,-1):
                    main_game.snake.direction = Vector2(0, 1)

                if event.key == pygame.K_UP and main_game.snake2.direction != (0,1):
                    main_game.snake2.direction = Vector2(0,-1)
                if event.key == pygame.K_LEFT and main_game.snake2.direction != (1,0):
                    main_game.snake2.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and main_game.snake2.direction != (-1,0):
                    main_game.snake2.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN and main_game.snake2.direction != (0,-1):
                    main_game.snake2.direction = Vector2(0, 1)

        screen.fill((183,41,219))
        #draw elements 
        main_game.draw_elements(True)
        pygame.display.update()

        clock.tick(60)
    
    else:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == SCREEN_UPDATE:
                single_main_game.update(False)
                single_main_game.winner(False)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and single_main_game.snake.direction != (0,1):
                    single_main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_LEFT and single_main_game.snake.direction != (1,0):
                    single_main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and single_main_game.snake.direction != (-1,0):
                    single_main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN and single_main_game.snake.direction != (0,-1):
                    single_main_game.snake.direction = Vector2(0, 1)
        
        screen.fill((183,41,219))
        #draw elements 
        single_main_game.draw_elements(False)
        pygame.display.update()

        clock.tick(60)
