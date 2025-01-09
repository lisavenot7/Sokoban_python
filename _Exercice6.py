try:  # import as appropriate for 2.x vs. 3.x
    import tkinter as tk
    import tkinter.messagebox as tkMessageBox
except:
    import Tkinter as tk
    import tkMessageBox

class Level(object):
    def __init__(self, root, xsbMatrix):
        self.root = root

        # calcul des dimensions de la matrice
        nbrows = len(xsbMatrix)
        nbcolumns = 0

        for line in xsbMatrix:
            nbc = len(line)
            if nbc > nbcolumns:
                nbcolumns = nbc

        self.height = nbrows * 64 
        self.width = nbcolumns * 64 
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="gray")
        self.canvas.pack(side="top", expand=True)

        # initialisation à vide de la matrice d'images
        self.matrix = []
        for lineIdx in range(nbrows):
            self.matrix.append([])
            for elemIdx in range(nbcolumns):
                self.matrix[lineIdx].append(None)

        y = 0
        for lineIdx in range(len(xsbMatrix)):
            x = 0
            for elemIdx in range(len(xsbMatrix[lineIdx])):
                e = xsbMatrix[lineIdx][elemIdx]
                if e == '#':
                    self.matrix[y][x] = tk.PhotoImage(file='wall.png')
                    self.canvas.create_image( # creation de l'image à la bonne position a completer)
                elif e == '@':
                    self.matrix[y][x] = tk.PhotoImage(file='PlayerDown.png')
                    self.playerId = # creation de l'image à la bonne position a completer
                    self.playerX = x
                    self.playerY = y
                else:
                    None
                x = x + 1
            y = y + 1
            x = 0
        self.canvas.tag_raise("movable","static")

class Sokoban(object):
    '''
    Main Level class
    '''

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sokoban")
        mat = [
            [' ', ' ', '#', '#', '#'],
            [' ', ' ', '#', '.', '#'],
            [' ', ' ', '#', ' ', '#', '#', '#', '#'],
            ['#', '#', '#', '$', ' ', '$', '.', '#'],
            ['#', '.', ' ', '$', '@', '#', '#', '#'],
            ['#', '#', '#', '#', '$', '#'],
            [' ', ' ', ' ', '#', '.', '#'],
            [' ', ' ', ' ', '#', '#', '#'] ]
        self.level = Level(self.root, mat)
 
    def play(self):
        self.root.mainloop()

Sokoban().play()
