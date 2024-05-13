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