def mirror(nb):
    return int(str(nb)[-1::-1])

def is_pal(nb):
    return nb == mirror(nb)

def next(u):
    if is_pal(u):
        return u
    return u + mirror(u)

def lyc(u0, n):
    if n != 0:
        return [u0] + lyc(next(u0), n - 1)
    return [u0]

print(lyc(97, 8))
