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

        self.root.bind("<Key>", self.keypressed)

        # on a besoin de deux matrices pour pouvoir déplacer les éléments déplacables
        # sans écraser les éléments non déplacables
        self.staticMatrix = []
        self.movableMatrix = []
        for lineIdx in range(nbrows):
            self.staticMatrix.append([])
            self.movableMatrix.append([])
            for elemIdx in range(nbcolumns):
                self.staticMatrix[lineIdx].append(None)
                self.movableMatrix[lineIdx].append(None)

        # Initialisation des matrices à partir de la matrice Xsb
        y = 0
        for lineIdx in range(len(xsbMatrix)):
            x = 0
            for elemIdx in range(len(xsbMatrix[lineIdx])):
                e = xsbMatrix[lineIdx][elemIdx]
                if e == '#':
                    image = tk.PhotoImage(file='wall.png')
                    self.staticMatrix[y][x] = # a completer
                    self.canvas.create_image(# a completer
                elif e == '@':
                    image = tk.PhotoImage(file='PlayerDown.png')
                    self.movableMatrix[y][x] = image
                    self.playerId = self.canvas.create_image(# a completer
                    self.playerX = x
                    self.playerY = y
                else:
                    None
                x = x + 1
            y = y + 1
            x = 0
        self.canvas.tag_raise("movable","static")

    def keypressed(self, event):
        x = self.playerX
        y = self.playerY
        # adapter les coordonnées du player en fonction du déplacement voulu
        if event.keysym == 'Up':
            self.playerY = self.playerY - 1
        elif event.keysym == 'Down':
            self.playerY = self.playerY + 1
        elif event.keysym == 'Left':
            self.playerX = self.playerX - 1
        else:
            self.playerX = self.playerX + 1
        # déplacer l'image dans la bonne case de movableMatrix
        self.movableMatrix[self.playerY][self.playerX] = self.movableMatrix[y][x]
        # l'ancienne case de movableMatrix est mise à jour
        self.movableMatrix[y][x] = None
        # supprimer l'ancienne image dans le canvas
        self.canvas.delete(self.playerId)
        # créer une nouvelle image dans le canvas à la bonne coordonnée
        self.playerId = self.canvas.create_image(self.playerX * 64, self.playerY * 64, image=self.movableMatrix[self.playerY][self.playerX], anchor=tk.NW, tag="movable")
            

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
