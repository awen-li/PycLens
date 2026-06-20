# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualSymmetryTest_test_relative_symmetry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args1 = [2456, 37.8, -12.45, Decimal('2.54'), Fraction(17, 54)]
    args2 = [2459, 37.2, -12.41, Decimal('2.59'), Fraction(15, 54)]
    assert len(args1) == len(args2)
    for (a, b) in zip(args1, args2):
        self.do_relative_symmetry(a, b)
