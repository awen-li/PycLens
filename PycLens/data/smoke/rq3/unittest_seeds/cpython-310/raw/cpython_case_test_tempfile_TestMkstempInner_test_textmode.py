# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstempInner_test_textmode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.do_create(bin=0)
    f.write(b'blat\x1a')
    f.write(b'extra\n')
    os.lseek(f.fd, 0, os.SEEK_SET)
    self.assertEqual(os.read(f.fd, 20), b'blat')
