#!/usr/bin/python3
import random

class MinesGame:
    def __init__(self, rows=8, cols=8, mines=10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.won = False
        
        self.place_mines()
        self.calculate_numbers()
    
    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mines_placed += 1
    
    def calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    continue
                count = 0
                for r in range(max(0, row-1), min(self.rows, row+2)):
                    for c in range(max(0, col-1), min(self.cols, col+2)):
                        if self.board[r][c] == -1:
                            count += 1
                self.board[row][col] = count
    
    def reveal(self, row, col):
        if self.game_over or self.won:
            return False
        
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        
        if self.revealed[row][col]:
            return False
        
        self.revealed[row][col] = True
        
        # Mina açıldı
        if self.board[row][col] == -1:
            self.game_over = True
            return True
        
        # 0 olan xanaları avtomatik aç
        if self.board[row][col] == 0:
            for r in range(max(0, row-1), min(self.rows, row+2)):
                for c in range(max(0, col-1), min(self.cols, col+2)):
                    if not self.revealed[r][c]:
                        self.reveal(r, c)
        
        # QALİBİYYƏT ŞƏRTİ - BU ƏSAS DÜZƏLİŞDİR
        self.check_win()
        
        return True
    
    def check_win(self):
        """Check if all non-mine cells are revealed"""
        total_non_mine = self.rows * self.cols - self.mines
        revealed_non_mine = 0
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != -1 and self.revealed[row][col]:
                    revealed_non_mine += 1
        
        if revealed_non_mine == total_non_mine:
            self.won = True
            self.game_over = True
            return True
        return False
    
    def display(self):
        print("  " + " ".join(str(i) for i in range(self.cols)))
        print("  " + "-" * (self.cols * 2))
        
        for row in range(self.rows):
            print(f"{row}|", end="")
            for col in range(self.cols):
                if not self.revealed[row][col]:
                    print("# ", end="")
                elif self.board[row][col] == -1:
                    print("* ", end="")
                elif self.board[row][col] == 0:
                    print(". ", end="")
                else:
                    print(f"{self.board[row][col]} ", end="")
            print()

def main():
    print("=== Mines Game (Debugging Task 3) ===")
    print("Reveal all non-mine cells to win!")
    print("# = hidden, . = empty, * = mine, number = adjacent mines")
    print()
    
    # Kiçik test oyunu
    game = MinesGame(rows=5, cols=5, mines=3)
    
    while not game.game_over:
        game.display()
        
        try:
            row = int(input("Enter row (0-4): "))
            col = int(input("Enter column (0-4): "))
            
            if not game.reveal(row, col):
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter valid numbers!")
            continue
        
        print()
    
    # Final board
    game.display()
    
    if game.won:
        print("\n🎉 CONGRATULATIONS! You won! 🎉")
        print("You revealed all non-mine cells!")
    else:
        print("\n💥 GAME OVER! You hit a mine! 💥")

if __name__ == "__main__":
    main()
