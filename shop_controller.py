import pygame as pg
from deck import Deck
from store import Store
from pet import Pet
from slot import Slot
from button import Button

class ShopController:
    # this class will maintain the shop and deck slot sets and handle interactions between them
    deck:Deck
    store:Store
    dragging_pet: Pet
    dragging_source_slot: Slot
    buttons: list[Button]

    def __init__(self, deck, store):
        self.deck = deck
        self.store = store
        self.dragging_pet = None
        self.buttons = []
        self.dragging_source_slot = None 

        # add button for rerolling shop
        self.reroll_button = Button(pg.Rect(10, 400, 100, 30), self.store.populate_store, text="Reroll Shop")
        self.buttons.append(self.reroll_button)
        
    def handle_mouse_down(self, pos: pg.Vector2):
        for button in self.buttons:
            if button.is_clicked(pos):
                button.activate()
                return

        # attempt to pick up a pet from either zone
        pet, source_slot = self.deck.find_pet_at_position(pos)
        if pet is None:
            pet, source_slot = self.store.find_pet_at_position(pos)

        if pet:
            self.dragging_pet = pet
            self.dragging_source_slot = source_slot
            pet.start_drag()
            # keep original position in case of invalid drop
            pet.original_pos = pg.Vector2(pet.pos)
            return
    
    def handle_mouse_up(self, pos: pg.Vector2):
        # finish dragging operation
        if not self.dragging_pet:
            return

        # determine where we released the mouse
        target_slot = self.deck.find_slot_at_position(pos) or self.store.find_slot_at_position(pos)

        def return_to_source():
            # restore pet position (slot already still holds it)
            self.dragging_pet.reset_position()

        if target_slot is None:
            # dropped outside any slot
            return_to_source()
        else:
            # same slot -> just return
            if target_slot is self.dragging_source_slot:
                target_slot.currentPet = self.dragging_pet
                self.dragging_pet.set_position(target_slot.pos)
            else:
                # handle cross‑zone rules
                if self.dragging_source_slot.isStoreSlot and not target_slot.isStoreSlot:
                    # buying from store into deck
                    if self.deck.money >= self.dragging_pet.cost:
                        self.deck.money -= self.dragging_pet.cost
                        target_slot.currentPet = self.dragging_pet
                        self.dragging_source_slot.currentPet = None
                        self.dragging_pet.set_position(target_slot.pos)
                    else:
                        return_to_source()
                elif not self.dragging_source_slot.isStoreSlot and not target_slot.isStoreSlot:
                    # swap two deck slots
                    self.swap_slot_pets(self.dragging_source_slot, target_slot)
                elif self.dragging_source_slot.isStoreSlot and target_slot.isStoreSlot:
                    # swap two store slots
                    return_to_source()  # for simplicity, disallow rearranging store
                else:
                    # deck -> store or other invalid move
                    return_to_source()

        # complete drag
        self.dragging_pet.stop_drag()
        self.dragging_pet = None
        self.dragging_source_slot = None

    def swap_slot_pets(self, slot1: Slot, slot2: Slot):
        """Swap the pets in two slots"""
        print("swapping pets between slots")
        pet1 = slot1.currentPet
        pet2 = slot2.currentPet
        
        slot1.currentPet = pet2
        if pet2:
            pet2.set_position(slot1.pos)
        
        slot2.currentPet = pet1
        if pet1:
            pet1.set_position(slot2.pos)

    def update_dragging_position(self, pos: pg.Vector2):
        """Update position of dragging pet to follow mouse"""
        if self.dragging_pet:
            self.dragging_pet.move_to(pos)

    def draw_dragging_pet(self, screen):
        if self.dragging_pet:
            # draw on top of everything
            self.dragging_pet.draw(screen, self.dragging_pet.pos)
        
    def draw(self, screen):
        self.deck.draw(screen)
        self.store.draw(screen)
        self.draw_dragging_pet(screen)
        self.reroll_button.draw(screen)