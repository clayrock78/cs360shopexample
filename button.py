import pygame as pg

class Button:
    rect: pg.Rect
    function: callable
    text: str

    def __init__(self, rect: pg.Rect, function: callable, text: str = ""):
        self.rect = rect
        self.function = function
        self.text = text

    def draw(self, screen):
        pg.draw.rect(screen, (150, 150, 150), self.rect)
        if self.text:
            font = pg.font.SysFont(None, 24)
            text_surf = font.render(self.text, True, (0, 0, 0))
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)
        

    def is_clicked(self, mouse_pos) -> bool:
        return self.rect.collidepoint(mouse_pos)
    
    def activate(self):
        self.function()
