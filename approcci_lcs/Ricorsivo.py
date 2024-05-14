__all__ = ['get_ric_lcs']

def _lcs_length(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    elif s1[m - 1] == s2[n - 1]:
        return 1 + _lcs_length(s1, s2, m - 1, n - 1)
    else:
        return max(_lcs_length(s1, s2, m, n - 1), _lcs_length(s1, s2, m - 1, n))


def get_ric_lcs(s1, s2):
    return _lcs_length(s1, s2, len(s1), len(s2))

