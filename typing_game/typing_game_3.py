#寿司打っぽくする
import pygame
import random
import time

pygame.init()

width = 800
height = 400

screen = pygame.display.set_mode((width, height))

pygame.display.set.caption('sushida')

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)
words = [
    'python',
    'pineapple',
    'coffee',
    'tea',
    'print'
]

current_word = random.choice(words)

word_x = 0
word_y = 50
word_speed = 2

typed_text = ''

score = 0
time_limit = 15

start_time = time.time()

clock = pygame.time.Clock()

def reset_game():
    global current_word
    global typed_text
    global score
    global start_time
    global game_over
    global word_x
    global word_y
    global word_speed
    
    current_word = random.choice(words)
    typed_text = ''
    score = 0
    word_x = 0
    word_y = 50
    word_speed = 2
    start_time =time.time()
    game_over = False
    
running = True

game_over = False

while running:
    elapsed_time = time.time()-start_time()
    remaining_time = max(0, int(time_limit - elapsed_time))
    
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                
                if typed_text == current_word:
                    score += 1
                else:
                    score -= 1
                
                current_word = random.choice(words)
                word_x = 50
                typed_text = ''
            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
        
            else:
                typed_text += event.unicode
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    reset_game()
            
    
            
        
    