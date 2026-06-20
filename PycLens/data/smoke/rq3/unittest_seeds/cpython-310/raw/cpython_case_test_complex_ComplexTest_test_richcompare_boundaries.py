# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_richcompare_boundaries

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(n, deltas, is_equal, imag=0.0):
        for delta in deltas:
            i = n + delta
            z = complex(i, imag)
            self.assertIs(complex.__eq__(z, i), is_equal(delta))
            self.assertIs(complex.__ne__(z, i), not is_equal(delta))
    for i in range(1, 10):
        pow = 52 + i
        mult = 2 ** i
        check(2 ** pow, range(1, 101), lambda delta: delta % mult == 0)
        check(2 ** pow, range(1, 101), lambda delta: False, float(i))
    check(2 ** 53, range(-100, 0), lambda delta: True)
