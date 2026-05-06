class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Initialize the DP array with 0s
        array_seq = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # Fill the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    array_seq[i][j] = 1 + array_seq[i - 1][j - 1]
                else:
                    array_seq[i][j] = max(array_seq[i - 1][j], array_seq[i][j - 1])

        # Uncomment the print statement if you want to debug the DP array
        # print(array_seq)
        
        # The bottom-right cell contains the length of the LCS
        return array_seq[m][n]
