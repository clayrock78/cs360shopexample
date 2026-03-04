import pygame as pg
from slot import Slot
from pet import Pet

class Slots:
    slots : list[Slot]

    def __init__(self, start_position: pg.Vector2, distance: int, size, numSlots: int, isStore:bool):
        self.slots = list()
        
        for i in range(numSlots):
            # make new empty slot objects
            self.slots.append(
                Slot(None, pg.Vector2(start_position.x + i * distance, start_position.y), isStoreSlot=isStore)
            )

    def find_pet_at_position(self, pos: pg.Vector2) -> tuple[Pet, Slot]:
        """Find a pet at the given position. Returns (pet, slot) or (None, None)"""
        for slot in self.slots:
            if slot.currentPet and slot.currentPet.is_mouse_over(pos):
                return slot.currentPet, slot
        return None, None

    def find_slot_at_position(self, pos: pg.Vector2) -> Slot:
        """Find a slot at the given position"""
        for slot in self.slots:
            if slot.contains_point(pos):
                return slot
        return None

    def draw(self, screen):
        # draw all slot backgrounds first so pets appear on top
        for slot in self.slots:
            slot.draw_circle(screen)
        # then draw pets in each slot (controller may hide dragging ones)
        for slot in self.slots:
            if slot.currentPet is not None and not slot.currentPet.is_dragging:
                slot.currentPet.draw(screen, slot.pos)
        
    def get_slot_at_pos(self, pos: pg.Vector2):
        for slot in self.slots:
            if (slot.pos - pos).length() < 50:
                return slot
        return None