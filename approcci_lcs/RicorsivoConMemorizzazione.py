def lcs_length(s1, s2, m, n, dp):
    if m == 0 or n == 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    if s1[m - 1] == s2[n - 1]:
        dp[m][n] = 1 + lcs_length(s1, s2, m - 1, n - 1, dp)
    else:
        dp[m][n] = max(lcs_length(s1, s2, m, n - 1, dp), lcs_length(s1, s2, m - 1, n, dp))
    return dp[m][n]


def get_lcs(s1, s2):
    dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    return lcs_length(s1, s2, len(s1), len(s2), dp)


class RicorsivoConMemorizzazione:
    length = 0
    string = ''

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    def lcs(self):
        self.length = lcs_length(self.s1, self.s2, len(self.s1), len(self.s2), self.dp)
        self.string = self.lcs_string()

    def lcs_string(self):
        m = len(self.s1)
        n = len(self.s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i = m
        j = n
        lcs = []
        while i > 0 and j > 0:
            if self.s1[i - 1] == self.s2[j - 1]:
                lcs.append(self.s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        return ''.join(lcs[::-1])

    def get_lcs_length(self):
        return self.length

    def get_lcs_string(self):
        return self.string
