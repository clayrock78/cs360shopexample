from slots import Slots
from slot import Slot
import pygame as pg

class Deck(Slots):
    money: int
    lives: int

    def __init__(self, start_position: pg.Vector2, distance: int, size, numSlots: int):
        super().__init__(start_position, distance, size, numSlots, isStore=False)

        self.money = 10
        self.lives = 3

        # create empty slots for the deck
        for i in range(numSlots):
            self.slots.append(
                Slot(None, pg.Vector2(start_position.x + i * distance, start_position.y), isStoreSlot=False)
            )


    def draw(self, screen):
        super().draw(screen)

        # Draw money and lives
        font = pg.font.SysFont(None, 24)
        BLACK = (0, 0, 0)
        money_text = font.render(f"Money: {self.money}", True, BLACK)
        lives_text = font.render(f"Lives: {self.lives}", True, BLACK)
        screen.blit(money_text, (10, 10))
        screen.blit(lives_text, (10, 40))
