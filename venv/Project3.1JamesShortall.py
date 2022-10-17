import arcade

my_window = arcade.open_window(1000, 900, "Graph Paper")
arcade.set_background_color(arcade.color.BANANA_MANIA)

arcade.start_render()
for xloc in range(50, 1000, 80):
    arcade.draw_line(xloc, 50, xloc, 800, arcade.color.CEDAR_CHEST, 5)
for yloc in range(50, 900, 80):
    arcade.draw_line(50, yloc, 1000, yloc, arcade.color.ELECTRIC_INDIGO, 5)
arcade.draw_circle_filled(100, 800, 50, arcade.color.LAVA)
arcade.draw_arc_filled(400, 700, 100,100, arcade.color.YELLOW, 40, 350)
arcade.draw_circle_filled(100, 700, 50, arcade.color.AERO_BLUE)
arcade.draw_circle_filled(100, 600, 50, arcade.color.LAVA)
arcade.draw_xywh_rectangle_outline(90, 600, 320, 250, arcade.color.LIGHT_CYAN, 5)
arcade.draw_triangle_outline(100, 700, 700, 800, 600, 400, arcade.color.HARLEQUIN, 8)
arcade.draw_text("James Shortall sorry for the seizure", 120.0, 300.0,
                 arcade.color.GREEN, 40, 80, 'left')

arcade.run()