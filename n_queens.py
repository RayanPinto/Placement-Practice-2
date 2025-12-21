def n_queens(n):
    drag1=set()
    drag2=set()
    sol=[]
    cols=set()
    board=['.'*n for i in range(n)]
    def place(row):
        if row==n:
            sol.append(board.copy())
            
            return
        for col in range(n):
            if col in cols or (row+col) in drag1 or (row-col) in drag2:
                continue
            cols.add(col);drag1.add(row+col);drag2.add(row-col)
            board[row]=board[row][:col]+"Q"+board[row][col+1:]
            place(row+1)
            cols.remove(col);drag1.remove(row+col);drag2.remove(row-col)
            board[row]=board[row][:col]+"."+board[row][col+1:]

    place(0)
    return sol


sol=n_queens(4)
for i,j in enumerate(sol,1):
    print(f"The total solutions are {i}:")
    print('\n'.join(j))