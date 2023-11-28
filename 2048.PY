import tkinter as tk
from random import randint

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")

        self.grid_size = 4
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]

        self.create_widgets()
        self.add_tile()
        self.add_tile()
        self.update_grid()

    def create_widgets(self):
        self.tiles = [[tk.Label(self.master, text="", width=5, height=2, font=("Helvetica", 16, "bold"), relief="ridge")
                       for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.tiles[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

    def add_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = empty_cells[randint(0, len(empty_cells) - 1)]
            self.grid[i][j] = 2 if randint(0, 9) < 9 else 4

    def update_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                self.tiles[i][j].configure(text=str(value), bg=self.get_tile_color(value))

    def get_tile_color(self, value):
        colors = {0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
                  32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                  1024: "#edc53f", 2048: "#edc22e"}
        return colors.get(value, "#ffffff")

    def move(self, direction):
        new_grid = self.grid

        for i in range(self.grid_size):
            row = self.grid[i]
            row = [value for value in row if value != 0]
            row = self.merge(row)
            row += [0] * (self.grid_size - len(row))
            new_grid[i] = row

        self.grid = list(map(list, zip(*new_grid))) if direction in ("Left", "Right") else new_grid
        self.add_tile()
        self.update_grid()

    def merge(self, row):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
        row = [value for value in row if value != 0]
        return row + [0] * (self.grid_size - len(row))

    def move_left(self, event):
        self.move("Left")

    def move_right(self, event):
        self.move("Right")

    def move_up(self, event):
        self.grid = list(map(list, zip(*self.grid)))
        self.move("Up")
        self.grid = list(map(list, zip(*self.grid)))

    def move_down(self, event):
        self.grid = list(map(list, zip(*self.grid[::-1])))
        self.move("Down")
        self.grid = list(map(list, zip(*self.grid[::-1])))


if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
