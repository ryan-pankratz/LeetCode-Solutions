class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = 0
        squareRow = 0
        squareCol = 0
        while count < 9:
            if not (self.isValidRow(board[count]) and self.isValidCol(board, count) and self.isValidSquare(board,
                                                                                                           squareRow,
                                                                                                           squareCol)):
                return False
            count += 1

            if count % 3 == 0:
                squareRow = 0
                squareCol = count
            else:
                squareRow += 3

        return True

    def isValidRow(self, row: List[str]) -> bool:
        seen = []
        for string in row:
            if string in seen:
                return False
            elif string.isdigit():
                seen.append(string)
        return True

    def isValidCol(self, board: List[List[str]], count: int) -> bool:
        seen = []
        for i in range(9):
            if board[i][count] in seen:
                return False
            elif board[i][count].isdigit():
                seen.append(board[i][count])
        return True

    def isValidSquare(self, board: List[List[str]], squareRow: int, squareCol: int) -> bool:
        seen = []
        for i in range(squareRow, squareRow + 3):
            for j in range(squareCol, squareCol + 3):
                if board[i][j] in seen:
                    return False
                elif board[i][j].isdigit():
                    seen.append(board[i][j])
        return True
