import pygame as pg
import random

class Pet:
    health: int
    attack: int
    cost: int
    is_dragging: bool
    original_pos: pg.Vector2

    def __init__(self, imageFilename):
        try:
            self.sprite = pg.image.load(f"images/{imageFilename}")
            self.sprite = pg.transform.scale(self.sprite, (100, 100))
            # key out white
            self.sprite.set_colorkey((255, 255, 255))
        except:
            # Placeholder if image not found
            self.sprite = pg.Surface((100, 100))
            self.sprite.fill((100, 150, 200))
        
        self.pos = pg.Vector2(0, 0)
        self.original_pos = pg.Vector2(0, 0)
        self.is_dragging = False
        self.cost = 3
        self.health = random.randint(1, 5)
        self.attack = random.randint(1, 5)

    def set_position(self, pos: pg.Vector2):
        """Set both current and original position"""
        self.pos = pg.Vector2(pos)
        self.original_pos = pg.Vector2(pos)

    def is_mouse_over(self, mouse_pos) -> bool:
        """Check if mouse is over the pet"""
        rect = self.sprite.get_rect()
        rect.center = self.pos
        return rect.collidepoint(mouse_pos)

    def start_drag(self):
        self.is_dragging = True

    def stop_drag(self):
        self.is_dragging = False

    def move_to(self, pos: pg.Vector2):
        """Move pet to a new position"""
        self.pos = pg.Vector2(pos)

    def reset_position(self):
        """Return pet to original position"""
        self.pos = pg.Vector2(self.original_pos)

    def draw(self, screen, pos):
        rect = self.sprite.get_rect()
        # If dragging, use current pos; otherwise use provided pos
        draw_pos = self.pos if self.is_dragging else pos
        rect.center = draw_pos
        screen.blit(self.sprite, rect)
    
        # draw health and attack in circles underneath this pet
        font = pg.font.SysFont(None, 24)
        BLACK = (0, 0, 0)
        # Health circle
        pg.draw.circle(screen, (255, 100, 100), (draw_pos.x - 20, draw_pos.y + 30), 15)
        health_text = font.render(str(self.health), True, BLACK)
        health_rect = health_text.get_rect(center=(draw_pos.x - 20, draw_pos.y + 30))
        screen.blit(health_text, health_rect)
        # Attack circle
        pg.draw.circle(screen, (100, 255, 100), (draw_pos.x + 20, draw_pos.y + 30), 15)
        attack_text = font.render(str(self.attack), True, BLACK)
        attack_rect = attack_text.get_rect(center=(draw_pos.x + 20, draw_pos.y + 30))
        screen.blit(attack_text, attack_rect)
