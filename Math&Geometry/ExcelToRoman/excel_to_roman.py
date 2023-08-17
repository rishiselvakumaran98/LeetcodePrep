class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for i in range(len(columnTitle)):
            col_num = col_num * 26 + (ord(columnTitle[i]) - ord('A') + 1)
        return col_num