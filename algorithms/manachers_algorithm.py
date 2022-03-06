def pallindromic_radii(s: str) -> str:
    dummy = "|"
    ss = dummy.join([c for c in s])
    n = len(ss)
    radii = [0 for i in range(n)]
    c = 0
    r = 0
    while c < n:
        while (
                (c - (r + 1) >= 0)
                and (c + (r + 1) < n)
                and (ss[c - (r + 1)] == ss[c + (r + 1)])):
            r += 1
        radii[c] = r
        c0 = c
        r0 = r
        c += 1
        r = 0
        while (c <= c0 + r0):
            cm = c0 - (c - c0)
            rm = r0 - (c - c0)
            if (radii[cm] < rm):
                radii[c] = radii[cm]
                c += 1
            elif (radii[cm] > rm):
                radii[c] = rm
                c += 1
            else:
                r = rm
                break
    cmax = -1
    rmax = -1
    max_count = -1
    for idx, r in enumerate(radii):
        if idx % 2 == 0:
            count = 2 * (r//2) + 1
        else:
            count = 2 * ((r + 1) // 2)
        if count > max_count:
            max_count = count
            cmax = idx
            rmax = r
    ret = ss[cmax - rmax: cmax + rmax + 1]
    ret = "".join(ret.split(dummy))
    return ret

if __name__=="__main__":
    s = "cbbd"
    print(pallindromic_radii(s))
