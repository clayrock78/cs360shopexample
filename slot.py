import pygame as pg
from pet import Pet
SLOT_COLOR = (200,200,200)

class Slot:
    pos: pg.Vector2
    size: float
    currentPet: Pet
    isStoreSlot: bool

    def __init__(self, pet:Pet, pos:pg.Vector2, isStoreSlot:bool):
        self.pos = pos
        self.size = 50
        self.isStoreSlot = isStoreSlot
        if pet:
            self.currentPet = pet
            self.currentPet.set_position(self.pos)
        else:
            self.currentPet = None

    def get_rect(self) -> pg.Rect:
        """Get the slot's bounding rectangle"""
        return pg.Rect(self.pos.x - self.size, self.pos.y - self.size, 
                       self.size * 2, self.size * 2)

    def contains_point(self, point: pg.Vector2) -> bool:
        """Check if a point is within this slot"""
        return self.get_rect().collidepoint(point)

    def draw_circle(self, screen):
        pg.draw.circle(screen, SLOT_COLOR, self.pos, self.size)

    def draw(self, screen):
        self.draw_circle(screen)
        # don't draw pet while it's being dragged (handled by controller)
        if self.currentPet is not None and not self.currentPet.is_dragging:
            self.currentPet.draw(screen, self.pos)
