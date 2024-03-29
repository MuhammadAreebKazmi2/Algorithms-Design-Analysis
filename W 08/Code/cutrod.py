def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

def cut_rod_memoized_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            q = max(q, p[i] + cut_rod_memoized_aux(p, n - i, r))
    r[n] = q
    return q

def cut_rod_memoize(p, n):
    r = [float('-inf')] * (n + 1)
    return cut_rod_memoized_aux(p, n, r)


def cut_rod_bottom_up(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]