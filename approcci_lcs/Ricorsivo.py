def lcs_length(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    elif s1[m - 1] == s2[n - 1]:
        return 1 + lcs_length(s1, s2, m - 1, n - 1)
    else:
        return max(lcs_length(s1, s2, m, n - 1), lcs_length(s1, s2, m - 1, n))


def get_lcs(s1, s2):
    return lcs_length(s1, s2, len(s1), len(s2))


class Ricorsivo:
    string = ''
    length = 0

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def lcs(self):
        self.length = lcs_length(self.s1, self.s2, len(self.s1), len(self.s2))
        self.string = self.lcs_string()

    def lcs_string(self):
        i = len(self.s1)
        j = len(self.s2)
        lcs = []
        while i > 0 and j > 0:
            if self.s1[i - 1] == self.s2[j - 1]:
                lcs.append(self.s1[i - 1])
                i -= 1
                j -= 1
            elif lcs_length(self.s1, self.s2, i, j - 1) > lcs_length(self.s1, self.s2, i - 1, j):
                j -= 1
            else:
                i -= 1
        return ''.join(lcs[::-1])

    def get_lcs_string(self):
        return self.string

    def get_lcs_length(self):
        return self.length
