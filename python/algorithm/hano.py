def hanoi_solver(n):
    def hano(n, src, dst, spare, ords):
        if n == 1:
            # src -> dst
            element = ords[src - 1].pop()
            ords[dst - 1].append(element)
            return f'{ords[0]} {ords[1]} {ords[2]}\n'

        res = ''
        # move n-1 to spare
        res += hano(n - 1, src, spare, dst, ords)
        # move last 1 to dst
        res += hano(1, src, dst, spare, ords)
        # move n-1 disks on spare to dst
        res += hano(n - 1, spare, dst, src, ords)

        return res

    if n <= 0:
        raise ValueError('disks must be greater than 0')

    ords = [list(range(n, 0, -1)), [], []]

    res = f'{ords[0]} {ords[1]} {ords[2]}\n'
    res += hano(n, 1, 3, 2, ords)
    return res


print(hanoi_solver(3))
