class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        cells = [[0]*(n+1) for zeros in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    cells[i][j] = cells[i-1][j-1] +  1
                else:
                    cells[i][j] = max(cells[i][j-1],cells[i-1][j])

        return cells[m][n]