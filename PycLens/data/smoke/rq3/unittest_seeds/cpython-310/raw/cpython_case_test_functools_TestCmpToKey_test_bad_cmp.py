# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCmpToKey_test_bad_cmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cmp1(x, y):
        raise ZeroDivisionError
    key = self.cmp_to_key(cmp1)
    with self.assertRaises(ZeroDivisionError):
        key(3) > key(1)

    class BadCmp:

        def __lt__(self, other):
            raise ZeroDivisionError

    def cmp1(x, y):
        return BadCmp()
    with self.assertRaises(ZeroDivisionError):
        key(3) > key(1)
