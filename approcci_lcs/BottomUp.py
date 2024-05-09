class BottomUp:
    length = 0
    string = ''

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.b = [[''] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    def lcs(self):
        self.length = self.lcs_length(self.s1, self.s2)
        self.string = self.lcs_string()

    def lcs_length(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    self.b[i][j] = '↖'
                elif dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    self.b[i][j] = '↑'
                else:
                    dp[i][j] = dp[i][j - 1]
                    self.b[i][j] = '←'
        return dp[m][n]

    def lcs_string(self):
        i = len(self.s1)
        j = len(self.s2)
        lcs = []
        while i > 0 and j > 0:
            if self.b[i][j] == '↖':
                lcs.append(self.s1[i - 1])
                i -= 1
                j -= 1
            elif self.b[i][j] == '↑':
                i -= 1
            else:
                j -= 1
        return ''.join(lcs[::-1])

    def get_lcs_length(self):
        return self.length

    def get_lcs_string(self):
        return self.string