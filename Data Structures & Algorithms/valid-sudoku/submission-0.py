class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            seen = set()
            for num in row:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)

        #check columns
        for j in range(9):
            seen = set()
            for i in range(9):
                num = board[i][j]
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)

        #check 3x3 squares
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[box_row * 3 + i][box_col * 3 + j]
                        if num != ".":
                            if num in seen:
                                return False
                            seen.add(num)   

        return True