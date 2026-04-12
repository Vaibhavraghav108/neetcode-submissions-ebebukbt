class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                char=board[r][c]
                if char == ".":
                    continue
                
                row=(char,"ROW",r)
                col=(char,"COL",c)
                box=(char,"BOX",r//3,c//3)
                if row in seen or col in seen or box in seen:
                    return False
                seen.add(row)
                seen.add(col)
                seen.add(box)
        return True

