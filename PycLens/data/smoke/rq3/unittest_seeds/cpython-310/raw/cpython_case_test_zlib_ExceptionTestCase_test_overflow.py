# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ExceptionTestCase_test_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(OverflowError, 'int too large'):
        zlib.decompress(b'', 15, sys.maxsize + 1)
    with self.assertRaisesRegex(OverflowError, 'int too large'):
        zlib.decompressobj().decompress(b'', sys.maxsize + 1)
    with self.assertRaisesRegex(OverflowError, 'int too large'):
        zlib.decompressobj().flush(sys.maxsize + 1)
