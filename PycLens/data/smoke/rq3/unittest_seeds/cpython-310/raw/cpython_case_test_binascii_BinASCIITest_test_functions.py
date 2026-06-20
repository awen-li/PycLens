# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_functions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in all_functions:
        self.assertTrue(hasattr(getattr(binascii, name), '__call__'))
        self.assertRaises(TypeError, getattr(binascii, name))
