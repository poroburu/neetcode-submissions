class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            values = [n for n in row if n != '.']
            if len(set(values)) != len(values):
                return False
        for col in range(len(board[0])):
            values = [row[col] for row in board if row[col] != '.']
            
            if len(set(values)) != len(values):
                return False
        
        for boxRow in range(0,9,3):
            for boxCol in range(0,9,3):
                values = []
            
                for row in range(boxRow, boxRow + 3):
                    for col in range(boxCol, boxCol + 3):
                        if board[row][col] != ".":
                            values.append(board[row][col])
                if len(values) != len(set(values)):
                    return False
        return True