from itertools import combinations


def subsequence_finder(s):  # O(2^n)
    out = set()
    for r in range(1, len(s) + 1):
        for c in combinations(s, r):
            out.add(''.join(c))
    return sorted(out)


class ForzaBruta:
    length = 0
    string = ''

    def __init__(self, s1, s2):
        self.s1_subsequences = subsequence_finder(s1)
        self.s2 = s2

    def lcs(self):
        self.length = self.lcs_length_and_string()

    def lcs_length_and_string(self):
        max_lcs_length = 0
        for sub in self.s1_subsequences[::-1]:
            temp_lcs_length = self._is_subsequence(sub)
            if temp_lcs_length > max_lcs_length:
                max_lcs_length = temp_lcs_length
                self.string = sub
        return max_lcs_length

    def _is_subsequence(self, subsequence):
        i = 0
        j = 0
        while j < len(self.s2) and i < len(subsequence):
            if subsequence[i] == self.s2[j]:
                i += 1
            j += 1
        return i

    def get_lcs_length(self):
        return self.length

    def get_lcs_string(self):
        return self.string
