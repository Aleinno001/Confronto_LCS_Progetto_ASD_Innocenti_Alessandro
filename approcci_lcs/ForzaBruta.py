__all__ = ['get_brute_force_lcs']

def _subseq(s):  # Funzione che restituisce tutte le sottosequenze di una stringa (=2^n)
    h = [""]
    n = len(s)
    for i in range(n):
        l = len(h)
        for j in range(l):
            h.append(h[j] + s[i])
    return h


def _is_subsequence(s2, subsequence):  # Funzione che restituisce la lunghezza della sottosequenza subsequence in s2
    i = 0
    j = 0
    while j < len(s2) and i < len(subsequence):
        if subsequence[i] == s2[j]:
            i += 1
        j += 1
    return i


def _lcs_length(s1_subsequences,
               s2):  # Funzione che restituisce la lunghezza della sottosequenza più lunga tra quelle generate
    max_lcs_length = 0
    for sub in s1_subsequences:
        temp_lcs_length = _is_subsequence(s2, sub)
        if temp_lcs_length > max_lcs_length:
            max_lcs_length = temp_lcs_length
    return max_lcs_length


def get_brute_force_lcs(s1, s2):
    s1_subsequences = _subseq(s1)
    return _lcs_length(s1_subsequences, s2)

