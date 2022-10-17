import arcade

file1 = open("venv/nationsPop.txt", "r")

some_lines = file1.readlines()

for lines in some_lines:
    lines= lines.split(',')

my_window = arcade.open_window(400,400, "Populations of Largest Nations on Earth")
arcade.set_background_color(arcade.color.LAVENDER)
arcade.start_render()
arcade.draw_line(80,400,80,80,arcade.color.HARLEQUIN)
arcade.draw_line(400,80,80,80,arcade.color.HARLEQUIN)
#arcade.draw
scale = (400-80) / len(range(100,1500,100))
currentY=80

for i in range(100,1500,100):
    currentLabel = arcade.Text(f"{1}M", 5, currentY, arcade.color.LAVENDER_MAGENTA)
    currentLabel.draw()
    currentY += scale

    arcade.finish_render()

    arcade.run()