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
        self.gap = 20
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.player_image = tk.PhotoImage(file='player.png')
        self.player_id = ... # a completer
        x, y= 0, self.canvas_height // 2

    def start_animation(self):
        # execute self.animation dans 10ms
        self.canvas.after(10, self.animation)

    def animation(self):
        # calcul du deplacement dans self.gap
        self.gap = 20
        x1, y1 = self.canvas.coords(self.player_id)
        if (x1 + self.player_image.width()) >= self.canvas_width:
            self.gap = -x1
        # deplacement du player
        self.canvas.move(self.player_id, self.gap, 0)
        # execute a nouveau self.animation dans 300ms
        self.canvas.after(300, self.animation)

    def start(self):
        self.start_animation()
        self.root.mainloop()


ex = Example()
ex.start()
