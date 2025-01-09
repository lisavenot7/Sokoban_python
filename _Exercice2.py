"""
@author: plantec
"""
try:  # import as appropriate for 2.x vs. 3.x
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox


class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        # A COMPLETER
        self.player_image = # a completer
        self.player_id = # a completer


    def keypress(self, event):
        # A MODIFIER
        if event.keysym == 'Left':
            print('gauche')
        elif event.keysym == 'Right':
            print('droite')
        elif event.keysym == 'space':
            print('espace')
 
    def start(self):
        self.install()
        # Quand n'importe quelle touche du clavier est appuyée, exécuter keypress
        self.root.bind("<Key>", self.keypress)
        self.root.mainloop()

ex = Example()
ex.start()
