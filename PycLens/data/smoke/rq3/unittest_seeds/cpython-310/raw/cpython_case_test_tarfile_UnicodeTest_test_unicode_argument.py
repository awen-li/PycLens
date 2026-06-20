# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UnicodeTest_test_unicode_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tarname, 'r', encoding='iso8859-1', errors='strict')
    try:
        for t in tar:
            self.assertIs(type(t.name), str)
            self.assertIs(type(t.linkname), str)
            self.assertIs(type(t.uname), str)
            self.assertIs(type(t.gname), str)
    finally:
        tar.close()
