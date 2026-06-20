# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_multiple_close_before_rollover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tempfile.SpooledTemporaryFile()
    f.write(b'abc\n')
    self.assertFalse(f._rolled)
    f.close()
    f.close()
    f.close()
