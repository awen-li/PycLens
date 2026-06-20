# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstemp_test_basic_with_bytes_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = tempfile.gettempdirb()
    self.do_create(dir=d, suf=b'')
    self.do_create(dir=d, pre=b'a')
    self.do_create(dir=d, suf=b'b')
    self.do_create(dir=d, pre=b'a', suf=b'b')
    self.do_create(dir=d, pre=b'aa', suf=b'.txt')
    self.do_create(dir=b'.')
    with self.assertRaises(TypeError):
        self.do_create(dir='.', pre=b'aa', suf=b'.txt')
    with self.assertRaises(TypeError):
        self.do_create(dir=b'.', pre='aa', suf=b'.txt')
    with self.assertRaises(TypeError):
        self.do_create(dir=b'.', pre=b'aa', suf='.txt')
