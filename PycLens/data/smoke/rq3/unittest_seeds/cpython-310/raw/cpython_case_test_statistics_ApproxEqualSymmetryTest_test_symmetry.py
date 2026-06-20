# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualSymmetryTest_test_symmetry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = [-23, -2, 5, 107, 93568]
    delta = 2
    for a in args:
        for type_ in (int, float, Decimal, Fraction):
            x = type_(a) * 100
            y = x + delta
            r = abs(delta / max(x, y))
            self.do_symmetry_test(x, y, tol=delta, rel=r)
            self.do_symmetry_test(x, y, tol=delta + 1, rel=2 * r)
            self.do_symmetry_test(x, y, tol=delta - 1, rel=r / 2)
            self.do_symmetry_test(x, y, tol=delta, rel=r / 2)
            self.do_symmetry_test(x, y, tol=delta - 1, rel=r)
            self.do_symmetry_test(x, y, tol=delta - 1, rel=2 * r)
            self.do_symmetry_test(x, x, tol=0, rel=0)
            self.do_symmetry_test(x, y, tol=0, rel=0)
