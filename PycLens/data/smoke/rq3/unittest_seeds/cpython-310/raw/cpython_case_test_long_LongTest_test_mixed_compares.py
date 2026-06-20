# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_mixed_compares

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual

    class Rat:

        def __init__(self, value):
            if isinstance(value, int):
                self.n = value
                self.d = 1
            elif isinstance(value, float):
                (f, e) = math.frexp(abs(value))
                assert f == 0 or 0.5 <= f < 1.0
                CHUNK = 28
                top = 0
                while f:
                    f = math.ldexp(f, CHUNK)
                    digit = int(f)
                    assert digit >> CHUNK == 0
                    top = top << CHUNK | digit
                    f -= digit
                    assert 0.0 <= f < 1.0
                    e -= CHUNK
                if e >= 0:
                    n = top << e
                    d = 1
                else:
                    n = top
                    d = 1 << -e
                if value < 0:
                    n = -n
                self.n = n
                self.d = d
                assert float(n) / float(d) == value
            else:
                raise TypeError("can't deal with %r" % value)

        def _cmp__(self, other):
            if not isinstance(other, Rat):
                other = Rat(other)
            (x, y) = (self.n * other.d, self.d * other.n)
            return (x > y) - (x < y)

        def __eq__(self, other):
            return self._cmp__(other) == 0

        def __ge__(self, other):
            return self._cmp__(other) >= 0

        def __gt__(self, other):
            return self._cmp__(other) > 0

        def __le__(self, other):
            return self._cmp__(other) <= 0

        def __lt__(self, other):
            return self._cmp__(other) < 0
    cases = [0, 0.001, 0.99, 1.0, 1.5, 1e+20, 1e+200]
    for t in (2.0 ** 48, 2.0 ** 50, 2.0 ** 53):
        cases.extend([t - 1.0, t - 0.3, t, t + 0.3, t + 1.0, int(t - 1), int(t), int(t + 1)])
    cases.extend([0, 1, 2, sys.maxsize, float(sys.maxsize)])
    t = int(1e+200)
    cases.extend([0, 1, 2, 1 << 20000, t - 1, t, t + 1])
    cases.extend([-x for x in cases])
    for x in cases:
        Rx = Rat(x)
        for y in cases:
            Ry = Rat(y)
            Rcmp = (Rx > Ry) - (Rx < Ry)
            with self.subTest(x=x, y=y, Rcmp=Rcmp):
                xycmp = (x > y) - (x < y)
                eq(Rcmp, xycmp)
                eq(x == y, Rcmp == 0)
                eq(x != y, Rcmp != 0)
                eq(x < y, Rcmp < 0)
                eq(x <= y, Rcmp <= 0)
                eq(x > y, Rcmp > 0)
                eq(x >= y, Rcmp >= 0)
