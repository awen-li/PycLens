# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstempInner_test_basic_with_bytes_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir_b = tempfile.gettempdirb()
    self.do_create(dir=dir_b, suf=b'').write(b'blat')
    self.do_create(dir=dir_b, pre=b'a').write(b'blat')
    self.do_create(dir=dir_b, suf=b'b').write(b'blat')
    self.do_create(dir=dir_b, pre=b'a', suf=b'b').write(b'blat')
    self.do_create(dir=dir_b, pre=b'aa', suf=b'.txt').write(b'blat')
    with self.assertRaises(TypeError):
        self.do_create(dir='', suf=b'').write(b'blat')
    with self.assertRaises(TypeError):
        self.do_create(dir=dir_b, pre='').write(b'blat')
    with self.assertRaises(TypeError):
        self.do_create(dir=dir_b, pre=b'', suf='').write(b'blat')
