# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_repr_large

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(n):
        l = [0] * n
        s = repr(l)
        self.assertEqual(s, '[' + ', '.join(['0'] * n) + ']')
    check(10)
    check(1000000)
