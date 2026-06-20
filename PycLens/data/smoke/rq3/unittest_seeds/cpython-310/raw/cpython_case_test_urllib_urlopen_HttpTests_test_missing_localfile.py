# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_missing_localfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(urllib.error.URLError) as e:
        urlopen('file://localhost/a/file/which/doesnot/exists.py')
    self.assertTrue(e.exception.filename)
    self.assertTrue(e.exception.reason)
