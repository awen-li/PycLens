# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_writelines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.do_create()
    f.writelines((b'x', b'y', b'z'))
    pos = f.seek(0)
    self.assertEqual(pos, 0)
    buf = f.read()
    self.assertEqual(buf, b'xyz')
