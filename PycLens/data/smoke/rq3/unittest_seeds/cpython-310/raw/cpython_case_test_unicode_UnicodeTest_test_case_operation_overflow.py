# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_case_operation_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = 2 ** 32 // 12 + 1
    try:
        s = 'ü' * size
    except MemoryError:
        self.skipTest('no enough memory (%.0f MiB required)' % (size / 2 ** 20))
    try:
        self.assertRaises(OverflowError, s.upper)
    finally:
        del s
