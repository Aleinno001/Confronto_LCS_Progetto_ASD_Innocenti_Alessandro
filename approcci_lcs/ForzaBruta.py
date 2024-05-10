from itertools import combinations


def subseq(s):
    h = [""]
    n = len(s)
    for i in range(n):
        l = len(h)
        for j in range(l):
            h.append(h[j] + s[i])
    return h


def _is_subsequence(s2, subsequence):
    i = 0
    j = 0
    while j < len(s2) and i < len(subsequence):
        if subsequence[i] == s2[j]:
            i += 1
        j += 1
    return i


def lcs_length(s1_subsequences, s2):
    max_lcs_length = 0
    for sub in s1_subsequences:
        temp_lcs_length = _is_subsequence(s2, sub)
        if temp_lcs_length > max_lcs_length:
            max_lcs_length = temp_lcs_length
    return max_lcs_length


def get_lcs(s1,s2):
    s1_subsequences = subseq(s1)
    return lcs_length(s1_subsequences, s2)

class ForzaBruta:
    length = 0
    string = ''

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def lcs(self):
        self.length = self.lcs_length_and_string()

    def lcs_length_and_string(self):
        max_lcs_length = 0
        for sub in subseq(self.s1):
            temp_lcs_length = _is_subsequence(self.s2, sub)
            if temp_lcs_length > max_lcs_length:
                max_lcs_length = temp_lcs_length
                self.string = sub
        return max_lcs_length

    def get_lcs_length(self):
        return self.length

    def get_lcs_string(self):
        return self.string
