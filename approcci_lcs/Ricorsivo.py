def lcs_length(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    elif s1[m - 1] == s2[n - 1]:
        return 1 + lcs_length(s1, s2, m - 1, n - 1)
    else:
        return max(lcs_length(s1, s2, m, n - 1), lcs_length(s1, s2, m - 1, n))


def get_lcs(s1, s2):
    return lcs_length(s1, s2, len(s1), len(s2))
