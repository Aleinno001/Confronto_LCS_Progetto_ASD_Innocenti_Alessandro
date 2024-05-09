class Ricorsivo:
    string = ''
    length = 0

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def lcs(self):
        self.length = self.lcs_length(len(self.s1), len(self.s2))
        self.string = self.lcs_string()

    def lcs_length(self, i, j):
        if i == 0 or j == 0:
            return 0
        if self.s1[i - 1] == self.s2[j - 1]:
            return 1 + self.lcs_length(i - 1, j - 1)
        return max(self.lcs_length(i, j - 1), self.lcs_length(i - 1, j))

    def lcs_string(self):
        i = len(self.s1)
        j = len(self.s2)
        lcs = []
        while i > 0 and j > 0:
            if self.s1[i - 1] == self.s2[j - 1]:
                lcs.append(self.s1[i - 1])
                i -= 1
                j -= 1
            elif self.lcs_length(i, j - 1) > self.lcs_length(i - 1, j):
                j -= 1
            else:
                i -= 1
        return ''.join(lcs[::-1])

    def get_lcs_string(self):
        return self.string

    def get_lcs_length(self):
        return self.length
