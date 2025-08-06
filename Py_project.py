import random

def unUsedInBox(grid, rowStart, colStart, num):
    for i in range(3):
        for j in range(3):
            if grid[rowStart + i][colStart + j] == num:
                return False
    return True

def fillBox(grid, row, col):
    for i in range(3):
        for j in range(3):
            while True:
                num = random.randint(1, 9)
                if unUsedInBox(grid, row, col, num):
                    break
            grid[row + i][col + j] = num

def unUsedInRow(grid, i, num):
    return num not in grid[i]

def unUsedInCol(grid, j, num):
    for i in range(9):
        if grid[i][j] == num:
            return False
    return True

def checkIfSafe(grid, i, j, num):
    return (unUsedInRow(grid, i, num) and
            unUsedInCol(grid, j, num) and
            unUsedInBox(grid, i - i % 3, j - j % 3, num))

def fillDiagonal(grid):
    for i in range(0, 9, 3):
        fillBox(grid, i, i)

def fillRemaining(grid, i, j):
    if i == 9:
        return True
    if j == 9:
        return fillRemaining(grid, i + 1, 0)
    if grid[i][j] != 0:
        return fillRemaining(grid, i, j + 1)
    for num in range(1, 10):
        if checkIfSafe(grid, i, j, num):
            grid[i][j] = num
            if fillRemaining(grid, i, j + 1):
                return True
            grid[i][j] = 0
    return False

def removeKDigits(grid, k):
    while k > 0:
        cellId = random.randint(0, 80)
        i = cellId // 9
        j = cellId % 9
        if grid[i][j] != 0:
            grid[i][j] = 0
            k -= 1

def sudokuGenerator(k):
    grid = [[0] * 9 for _ in range(9)]
    fillDiagonal(grid)
    fillRemaining(grid, 0, 0)
    removeKDigits(grid, k)
    return grid

import tkinter as tk
from tkinter import messagebox
import random

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Generator")

        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        self.root.minsize(380, 420)

        for i in range(9):
            for j in range(9):
                padx = 3 if j % 3 == 0 and j != 0 else 1
                pady = 3 if i % 3 == 0 and i != 0 else 1

                if (i // 3 + j // 3) % 2 == 0:
                    bg_color = '#d1ffbd' 
                else:
                    bg_color = '#ffffff'  

                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center', borderwidth=2,
                         relief='ridge', bg=bg_color)
                entry.grid(row=i, column=j, padx=padx, pady=pady)
                self.cells[i][j] = entry
        

    
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.grid(row=10, column=0, columnspan=9, pady=(10, 0))

        easy_btn = tk.Button(button_frame, text="Easy", command=self.generate_puzzleE,
                             bg='#b2fab4', font=('Arial', 11, 'bold'), width=8)
        easy_btn.grid(row=0, column=0, padx=5)

        medium_btn = tk.Button(button_frame, text="Medium", command=self.generate_puzzleM,
                               bg='#fff176', font=('Arial', 11, 'bold'), width=8)
        medium_btn.grid(row=0, column=1, padx=5)

        hard_btn = tk.Button(button_frame, text="Hard", command=self.generate_puzzleH,
                             bg='#ff8a65', font=('Arial', 11, 'bold'), width=8)
        hard_btn.grid(row=0, column=2, padx=5)

        clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_grid,
                              bg='lightcoral', font=('Arial', 11, 'bold'), width=8)
        clear_btn.grid(row=0, column=3, padx=5)

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
    def generate_puzzleE(self):
        sudoku = sudokuGenerator(35)
        self.clear_grid()
        for col in range(9):
            for roow in range(9):
                if(sudoku[roow][col]==0):
                    continue
                self.cells[roow][col].insert(0,sudoku[roow][col])
    def generate_puzzleM(self):
        sudoku = sudokuGenerator(43)
        self.clear_grid()
        for col in range(9):
            for roow in range(9):
                if(sudoku[roow][col]==0):
                    continue
                self.cells[roow][col].insert(0,sudoku[roow][col])
    def generate_puzzleH(self):
        sudoku = sudokuGenerator(51)
        self.clear_grid()
        for col in range(9):
            for roow in range(9):
                if(sudoku[roow][col]==0):
                    continue
                self.cells[roow][col].insert(0,sudoku[roow][col])
                 
root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()

