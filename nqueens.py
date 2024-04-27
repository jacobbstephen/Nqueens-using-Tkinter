import  tkinter as tk
# we need 3 fn
class NqueensGui:
    def __init__(self, master,size):
        self.master = master
        self.size = size
        self.board = [[0] * size for _ in range(size)] # 2 dim array => with all elements as 0
        self.queens = []
        
        #use a canvas widget
        self.canvas = tk.Canvas(master,width=500, height = 500)
        self.canvas.pack()
        self.draw_board()
        self.solve(0)
        self.display_solution()
    def draw_board(self):
        color = ["gray", "black"]
        for i in range(self.size):
            for j in range(self.size):
                # calculate the top left corner postion for each row
                x0, y0 = i * 500 / self.size, j * 500 / self.size
                # to get the bottom right corner postion
                x1, y1 = (i + 1) * 500 / self.size, (j + 1) * 500 / self.size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[(i + j) % 2])
    def isSafe(self,row,col):
        #vertical up
        for i in range(row-1, -1, -1):
            if self.board[i][col] == 1:
                return False
        #diagonal left
        for i, j in zip(range(row - 1, -1, -1), range(col -1,-1, -1)):
            if self.board[i][j] == 1:
                return False

        #Diagonal right
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, self.size, + 1)):
            if self.board[i][j] == 1:
                return False
        return True
        
    def solve(self, row):
        if row == self.size:
            return  True
        for  col in range(self.size):
            if self.isSafe(row,col):
                self.queens.append((row, col))
                self.board[row][col] = 1
                if self.solve(row + 1):
                    return True
                self.queens.remove((row, col))
                self.board[row][col] = 0
    
    def display_solution(self):
        print("Queens:", self.queens)
        for queen in self.queens:
            x0, y0 = queen[1] * 500 / self.size, queen[0] * 500 / self.size
            x1, y1 = (queen[1] + 1) * 500 / self.size, (queen[0] + 1) * 500 / self.size
            self.canvas.create_oval(x0, y0, x1, y1, fill="white")
        
        

def main():
    size = 4
    #create a window
    root = tk.Tk()
    root.title("N Queens solver")
    gui = NqueensGui(root,size)
    root.mainloop()
if __name__ == "__main__":
    main()