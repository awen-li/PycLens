# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_ftp_nohost

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_ftp_url = 'ftp:///path'
    with self.assertRaises(urllib.error.URLError) as e:
        urlopen(test_ftp_url)
    self.assertFalse(e.exception.filename)
    self.assertTrue(e.exception.reason)
