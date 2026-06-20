# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_write_sequential

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.do_create(max_size=30)
    self.assertFalse(f._rolled)
    f.write(b'x' * 20)
    self.assertFalse(f._rolled)
    f.write(b'x' * 10)
    self.assertFalse(f._rolled)
    f.write(b'x')
    self.assertTrue(f._rolled)
