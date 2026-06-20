# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_constructor_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadInt:

        def __index__(self):
            1 / 0
    self.assertRaises(ZeroDivisionError, self.type2test, BadInt())
    self.assertRaises(ZeroDivisionError, self.type2test, [BadInt()])

    class BadIterable:

        def __iter__(self):
            1 / 0
    self.assertRaises(ZeroDivisionError, self.type2test, BadIterable())
