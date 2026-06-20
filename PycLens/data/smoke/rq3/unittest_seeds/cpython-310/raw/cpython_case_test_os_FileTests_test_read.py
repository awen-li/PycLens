# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'w+b') as fobj:
        fobj.write(b'spam')
        fobj.flush()
        fd = fobj.fileno()
        os.lseek(fd, 0, 0)
        s = os.read(fd, 4)
        self.assertEqual(type(s), bytes)
        self.assertEqual(s, b'spam')
