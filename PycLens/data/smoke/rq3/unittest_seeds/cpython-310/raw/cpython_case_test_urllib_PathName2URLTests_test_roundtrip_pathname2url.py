# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: PathName2URLTests_test_roundtrip_pathname2url

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    list_of_paths = ['///C:', '/////folder/test/', '///C:/foo/bar/spam.foo']
    for path in list_of_paths:
        self.assertEqual(pathname2url(url2pathname(path)), path)
