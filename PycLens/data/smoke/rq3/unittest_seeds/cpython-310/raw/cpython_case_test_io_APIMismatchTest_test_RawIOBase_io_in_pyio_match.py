# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: APIMismatchTest_test_RawIOBase_io_in_pyio_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mismatch = support.detect_api_mismatch(pyio.RawIOBase, io.RawIOBase, ignore=('__weakref__',))
    self.assertEqual(mismatch, set(), msg='Python RawIOBase does not have all C RawIOBase methods')
