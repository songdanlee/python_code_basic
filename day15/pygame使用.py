import sys
import pygame


SCRREN_WIDTH = 1000
SCRREN_HEIGHT = 700


class MainGame():
    windows = None
    def create_window(self):
        pygame.display.init()
        # 创建窗口
        MainGame.windows = pygame.display.set_mode((SCRREN_WIDTH,SCRREN_HEIGHT))
        pygame.display.set_caption("坦克大战")

    def start_game(self):
        self.create_window()
        while True:
            # 屏幕刷新
            pygame.display.update()
            self.deal_event()

    def deal_event(self):
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()


MainGame().start_game()