class Ricorsivo:
    actual_lcs = []
    lcs_lenght = 0

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def lcs_length(self, i, j):
        if i == 0 or j == 0:
            return 0
        if self.s1[i - 1] == self.s2[j - 1]:
            self.actual_lcs.append(self.s1[i - 1])      # aggiungo il carattere alla sequenza
            return 1 + self.lcs_length(i - 1, j - 1)
        return max(self.lcs_length(i, j - 1), self.lcs_length(i - 1, j))

    def get_lcs(self):
        return ''.join(self.actual_lcs[::-1])

    def get_length(self):
        return self.lcs_lenght

    def lcs(self):
        self.lcs_length(len(self.s1), len(self.s2))
        return self.get_lcs()