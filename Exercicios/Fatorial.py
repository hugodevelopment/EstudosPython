def _mf_r(n, i, a):
    if i <= n:
        a.append(fatorial(i))
        _mf_r(n, i + 1, a)
    return a

def mf_r(n):
    return _mf_r(n, 1, [])

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fatorial(x - 1)

print(mf_r(5))