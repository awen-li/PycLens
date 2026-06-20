# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_conversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class JustLong:

        def __long__(self):
            return 42
    self.assertRaises(TypeError, int, JustLong())

    class LongTrunc:

        def __long__(self):
            return 42

        def __trunc__(self):
            return 1729
    self.assertEqual(int(LongTrunc()), 1729)
