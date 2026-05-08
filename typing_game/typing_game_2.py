#時間制限を追加
#ゲームオーバー画面を追加
#リスタート機能を追加
import pygame
import random
import time   #変更点　timeモジュール追加

# pygameを開始
pygame.init()

# 画面サイズ
WIDTH = 800
HEIGHT = 400

# ウィンドウ作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# タイトル
pygame.display.set_caption("Typing Game")

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# フォント
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# 単語リスト
words = [
    "python",
    "apple",
    "banana",
    "keyboard",
    "science",
    "computer"
]

# ランダムに単語選択
current_word = random.choice(words)

# 入力中の文字
typed_text = ""

# スコア
score = 0

#制限時間設定
time_limit = 10

#開始時間
start_time = time.time()  #現在時間を秒で取得

# 時間管理
clock = pygame.time.Clock()

#初期化関数を作成・・・・・・・・・・・・・・・・・・・・・・・・
def reset_game():
    global current_word
    global typed_text
    global score
    global start_time
    global game_over
    
    current_word = random.choice(words)
    typed_text = ''
    score = 0
    start_time =time.time()
    game_over = False
    

# ゲーム継続
running = True

#gameover
game_over = False

# メインループ
while running:
    
    #経過時間
    elapsed_time = time.time() - start_time
    
    #残り時間
    remaining_time = max(0, int(time_limit - elapsed_time)) #max(0, ) 0未満防止

    # 背景を白に
    screen.fill(WHITE)

    # イベント取得
    for event in pygame.event.get():

        # ×ボタンで終了
        if event.type == pygame.QUIT:
            running = False

        # キーボード入力
        if event.type == pygame.KEYDOWN and not game_over: #変更点 ゲームオーバー後は入力禁止

            # Enterキー
            if event.key == pygame.K_RETURN:

                # 正解判定
                if typed_text == current_word:
                    score += 1
                else:
                    score -=1
                
                current_word = random.choice(words)
                typed_text = ""

            # バックスペース
            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]

            # 普通の文字入力
            else:
                typed_text += event.unicode
        
        #ゲームオーバー時、ESCキーで終了
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:  #Rキーでリスタート・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
                    reset_game()

    #時間切れ判定
    if remaining_time <= 0 and not game_over:
        game_over = True
        
    if not game_over: #通常の画面
        #単語の描画
        word_surface = font.render(current_word, True, BLACK)
        screen.blit(word_surface, (250, 100))

        # 入力文字描画
        text_surface = small_font.render(typed_text, True, BLACK)
        screen.blit(text_surface, (250, 220))

        # スコア描画
        score_surface = small_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surface, (20, 20))
        
        #残り時間の描画
        time_surface = small_font.render(f'Time: {remaining_time}', True, BLACK)
        screen.blit(time_surface, (20, 70))
    else:
        #ゲームオーバー画面
        game_over_surface = font.render('GAME OVER', True, BLACK)
        screen.blit(game_over_surface, (180, 100))
        
        #点数表示
        final_score_surface = small_font.render(f'Final Score: {score}', True, BLACK)
        screen.blit(final_score_surface, (260, 220))
        
        #終了ボタン
        exit_surface = small_font.render("Press ESC to quit", True, BLACK)
        screen.blit(exit_surface, (220, 300))
        
        #リスタート画面・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
        restart_surface = small_font.render('Press R to Restart', True, BLACK)
        screen.blit(restart_surface, (220, 260))
        

    # 画面更新
    pygame.display.update()

    # FPS
    clock.tick(60)

pygame.quit()