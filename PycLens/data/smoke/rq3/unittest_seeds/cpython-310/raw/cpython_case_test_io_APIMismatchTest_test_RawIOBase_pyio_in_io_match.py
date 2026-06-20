# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: APIMismatchTest_test_RawIOBase_pyio_in_io_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mismatch = support.detect_api_mismatch(io.RawIOBase, pyio.RawIOBase)
    self.assertEqual(mismatch, set(), msg='C RawIOBase does not have all Python RawIOBase methods')
