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
    def __init__(self, canvas, y, speed):
        self.canvas = canvas
        self.canvas_width = # a completer
        self.player_image = # a completer
        self.player_id = # a completer
        self.speed = speed

    def moveOrComeBack(self):
        # calcul du deplacement dans self.gap
        self.gap = self.speed
            # a completer
        # deplacement du player
            # a completer

class MobileFleet:
    def __init__(self, canvas):
        self.fleet = []
        self.fleet.append(Mobile(canvas, 10, 10))
        self.fleet.append(# a completer
        self.fleet.append(# a completer
        self.fleet.append(# a completer

    def moveOrComeBack(self):
        for m in self.fleet:
            m.moveOrComeBack()

class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.fleet = MobileFleet(self.canvas)
        self.canvas.pack()

    def start_animation(self):
        # execute self.animation dans 10ms
        self.canvas.after(10, self.animation)

    def animation(self):
        self.fleet.moveOrComeBack()
        # execute a nouveau self.animation dans 300ms
        self.canvas.after(300, self.animation)

    def start(self):
        self.start_animation()
        self.root.mainloop()


ex = Example()
ex.start()
