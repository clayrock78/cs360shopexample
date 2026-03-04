import pygame as pg
from shop_controller import ShopController
from deck import Deck
from slots import Slots
from store import Store
pg.init()

screen = pg.display.set_mode((int(1920/2), int(1080/2)))
pg.display.set_caption("Pet Shop - Drag pets to move them")

deck = Deck(pg.Vector2(100, 150), 180, 30, 5)
store = Store(pg.Vector2(100, 300), 180, 30, 5)
shop_controller = ShopController(deck, store)


running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pg.Vector2(event.pos)
                shop_controller.handle_mouse_down(mouse_pos)
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                mouse_pos = pg.Vector2(event.pos)
                shop_controller.handle_mouse_up(mouse_pos)
        elif event.type == pg.MOUSEMOTION:
            mouse_pos = pg.Vector2(event.pos)
            shop_controller.update_dragging_position(mouse_pos)
    
    screen.fill((255, 255, 255))
    shop_controller.draw(screen)

        
    pg.display.flip()
    clock.tick(60)

pg.quit()