# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: LinkTests_test_unicode_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.fsencode('ñ')
    except UnicodeError:
        raise unittest.SkipTest('Unable to encode for this platform.')
    self.file1 += 'ñ'
    self.file2 = self.file1 + '2'
    self._test_link(self.file1, self.file2)
