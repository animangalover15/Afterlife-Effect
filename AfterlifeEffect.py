import Tkinter, tkFont
root = Tkinter.TK()
root.title("Afterlife Effect")

canvas = Tkinter.Canvas(root, height = 600, width = 800, relief = Tkinter.RAISED, bg = 'white')
canvas.grid(row = 0, column = 0)

TitleScreen = Tkinter.titlescreen(root, text = "Start")
