"""
@author: plantec
"""
try:  # import as appropriate for 2.x vs. 3.x
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox


class Mobile:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas_width = int(self.canvas.cget("width"))
        self.player_image = # a completer
        self.player_id = # a completer

    def moveOrComeBack(self):
        # calcul du deplacement dans self.gap
        self.gap = 20
            # a completer
        # deplacement du player
            # a completer
        

class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        
        self.mob = Mobile(self.canvas)

    def start_animation(self):
        # execute self.animation dans 10ms
        self.canvas.after(10, self.animation)

    def animation(self):
        self.mob.moveOrComeBack()
        # execute a nouveau self.animation dans 300ms
        self.canvas.after(300, self.animation)

    def start(self):
        self.start_animation()
        self.root.mainloop()


ex = Example()
ex.start()
