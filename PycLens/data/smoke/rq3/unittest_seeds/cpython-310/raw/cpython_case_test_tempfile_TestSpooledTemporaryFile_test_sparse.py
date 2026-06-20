# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_sparse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.do_create(max_size=30)
    self.assertFalse(f._rolled)
    pos = f.seek(100, 0)
    self.assertEqual(pos, 100)
    self.assertFalse(f._rolled)
    f.write(b'x')
    self.assertTrue(f._rolled)
