class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #validate rows
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])       
       #validate columns
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
        #validate boxes
        starts=[(0,0),(0,3),(0,6),
        (3,0),(3,3),(3,6),
        (6,0),(6,3),(6,6)]
        for r, c in starts:
            s = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        return True