# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_ftp_nonexisting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(urllib.error.URLError) as e:
        urlopen('ftp://localhost/a/file/which/doesnot/exists.py')
    self.assertFalse(e.exception.filename)
    self.assertTrue(e.exception.reason)
