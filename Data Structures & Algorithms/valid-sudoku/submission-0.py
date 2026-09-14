class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current = set()

        # Check rows
        for row in board:
            for num in row:
                if num != '.':
                    if num in current:
                        return False
                    current.add(num)
            current.clear()
        
        # Check columns
        for col in range(9):
            for row in range(9):
                num = board[row][col]
                if num != '.':
                    if num in current:
                        return False
                    current.add(num)
            current.clear()
        
        # Check 3*3 grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        num = board[x][y]
                        if num != '.':
                            if num in current:
                                return False
                            current.add(num)
                current.clear()

        return True