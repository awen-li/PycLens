# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_hash_optional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from itertools import product
    if not RUN_ALL_HASH_TESTS:
        return

    def tryone_inner(tag, nbins, hashes, expected=None, zlimit=None):
        from collections import Counter
        nballs = len(hashes)
        (mean, sdev) = support.collision_stats(nbins, nballs)
        c = Counter(hashes)
        collisions = nballs - len(c)
        z = (collisions - mean) / sdev
        pileup = max(c.values()) - 1
        del c
        got = (collisions, pileup)
        failed = False
        prefix = ''
        if zlimit is not None and z > zlimit:
            failed = True
            prefix = f'FAIL z > {zlimit}; '
        if expected is not None and got != expected:
            failed = True
            prefix += f'FAIL {got} != {expected}; '
        if failed or JUST_SHOW_HASH_RESULTS:
            msg = f'{prefix}{tag}; pileup {pileup:,} mean {mean:.1f} '
            msg += f'coll {collisions:,} z {z:+.1f}'
            if JUST_SHOW_HASH_RESULTS:
                import sys
                print(msg, file=sys.__stdout__)
            else:
                self.fail(msg)

    def tryone(tag, xs, native32=None, native64=None, hi32=None, lo32=None, zlimit=None):
        NHASHBITS = support.NHASHBITS
        hashes = list(map(hash, xs))
        tryone_inner(tag + f'; {NHASHBITS}-bit hash codes', 1 << NHASHBITS, hashes, native32 if NHASHBITS == 32 else native64, zlimit)
        if NHASHBITS > 32:
            shift = NHASHBITS - 32
            tryone_inner(tag + '; 32-bit upper hash codes', 1 << 32, [h >> shift for h in hashes], hi32, zlimit)
            mask = (1 << 32) - 1
            tryone_inner(tag + '; 32-bit lower hash codes', 1 << 32, [h & mask for h in hashes], lo32, zlimit)
    tryone('range(100) by 3', list(product(range(100), repeat=3)), (0, 0), (0, 0), (4, 1), (0, 0))
    cands = list(range(-10, -1)) + list(range(9))
    tryone('-10 .. 8 by 4', list(product(cands, repeat=4)), (0, 0), (0, 0), (0, 0), (0, 0))
    del cands
    L = [n << 60 for n in range(100)]
    tryone('0..99 << 60 by 3', list(product(L, repeat=3)), (0, 0), (0, 0), (0, 0), (324, 1))
    del L
    tryone('[-3, 3] by 18', list(product([-3, 3], repeat=18)), (7, 1), (0, 0), (7, 1), (6, 1))
    tryone('[0, 0.5] by 18', list(product([0, 0.5], repeat=18)), (5, 1), (0, 0), (9, 1), (12, 1))
    tryone('4-char tuples', list(product('abcdefghijklmnopqrstuvwxyz', repeat=4)), zlimit=4.0)
    N = 50
    base = list(range(N))
    xp = list(product(base, repeat=2))
    inps = base + list(product(base, xp)) + list(product(xp, base)) + xp + list(zip(base))
    tryone('old tuple test', inps, (2, 1), (0, 0), (52, 49), (7, 1))
    del base, xp, inps
    n = 5
    A = [x for x in range(-n, n + 1) if x != -1]
    B = A + [(a,) for a in A]
    L2 = list(product(A, repeat=2))
    L3 = L2 + list(product(A, repeat=3))
    L4 = L3 + list(product(A, repeat=4))
    T = A
    T += [(a,) for a in B + L4]
    T += product(L3, B)
    T += product(L2, repeat=2)
    T += product(B, L3)
    T += product(B, B, L2)
    T += product(B, L2, B)
    T += product(L2, B, B)
    T += product(B, repeat=4)
    assert len(T) == 345130
    tryone('new tuple test', T, (9, 1), (0, 0), (21, 5), (6, 1))
