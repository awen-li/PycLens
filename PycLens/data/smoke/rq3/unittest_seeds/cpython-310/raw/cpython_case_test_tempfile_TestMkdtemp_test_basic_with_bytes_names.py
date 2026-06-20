# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkdtemp_test_basic_with_bytes_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = tempfile.gettempdirb()
    os.rmdir(self.do_create(dir=d))
    os.rmdir(self.do_create(dir=d, pre=b'a'))
    os.rmdir(self.do_create(dir=d, suf=b'b'))
    os.rmdir(self.do_create(dir=d, pre=b'a', suf=b'b'))
    os.rmdir(self.do_create(dir=d, pre=b'aa', suf=b'.txt'))
    with self.assertRaises(TypeError):
        os.rmdir(self.do_create(dir=d, pre='aa', suf=b'.txt'))
    with self.assertRaises(TypeError):
        os.rmdir(self.do_create(dir=d, pre=b'aa', suf='.txt'))
    with self.assertRaises(TypeError):
        os.rmdir(self.do_create(dir='', pre=b'aa', suf=b'.txt'))
