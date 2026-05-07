import pygame
import random

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

# 時間管理
clock = pygame.time.Clock()

# ゲーム継続
running = True

# メインループ
while running:

    # 背景を白に
    screen.fill(WHITE)

    # イベント取得
    for event in pygame.event.get():

        # ×ボタンで終了
        if event.type == pygame.QUIT:
            running = False

        # キーボード入力
        if event.type == pygame.KEYDOWN:

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

    # 単語描画
    word_surface = font.render(current_word, True, BLACK)
    screen.blit(word_surface, (250, 100))

    # 入力文字描画
    text_surface = small_font.render(typed_text, True, BLACK)
    screen.blit(text_surface, (250, 220))

    # スコア描画
    score_surface = small_font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surface, (20, 20))

    # 画面更新
    pygame.display.update()

    # FPS
    clock.tick(60)

pygame.quit()