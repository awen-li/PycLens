# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_dbcheck

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dbcheck('args[1] is not None')
    def f(a, b):
        return a + b
    self.assertEqual(f(1, 2), 3)
    self.assertRaises(DbcheckError, f, 1, None)
