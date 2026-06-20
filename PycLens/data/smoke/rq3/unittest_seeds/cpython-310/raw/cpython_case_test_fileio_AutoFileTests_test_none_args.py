# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileio.py
# case: AutoFileTests_test_none_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.f.write(b'hi\nbye\nabc')
    self.f.close()
    self.f = self.FileIO(TESTFN, 'r')
    self.assertEqual(self.f.read(None), b'hi\nbye\nabc')
    self.f.seek(0)
    self.assertEqual(self.f.readline(None), b'hi\n')
    self.assertEqual(self.f.readlines(None), [b'bye\n', b'abc'])
