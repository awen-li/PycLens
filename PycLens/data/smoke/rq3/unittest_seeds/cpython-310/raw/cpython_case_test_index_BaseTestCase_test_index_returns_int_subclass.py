# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: BaseTestCase_test_index_returns_int_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadInt:

        def __index__(self):
            return True

    class BadInt2(int):

        def __index__(self):
            return True
    bad_int = BadInt()
    with self.assertWarns(DeprecationWarning):
        n = operator.index(bad_int)
    self.assertEqual(n, 1)
    bad_int = BadInt2()
    n = operator.index(bad_int)
    self.assertEqual(n, 0)
