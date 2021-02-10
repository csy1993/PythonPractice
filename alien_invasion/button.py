import pygame.font
class Button():
    def __init__(self, aisettings, screen,msg):
        """初始化按钮的属性"""
        self.screen=screen
        self.screen_rect=screen.get_rect()
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message only needs to be prepped once.
        self.prep_msg(msg)