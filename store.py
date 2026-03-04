import pygame as pg
from slot import Slot
from pet import Pet
from slots import Slots
import random

# store inherit from slots
class Store (Slots):
    def __init__(self, start_position: pg.Vector2, distance: int, size, numSlots: int):
        super().__init__(start_position, distance, size, numSlots, isStore=True)
        self.populate_store()

    
    def populate_store(self):
        """Populate the store with new pets. For simplicity, we just create new pet instances."""
        for slot in self.slots:
            pet = Pet(f"{random.randint(0,2)}.png")
            pet.set_position(slot.pos)
            slot.currentPet = pet