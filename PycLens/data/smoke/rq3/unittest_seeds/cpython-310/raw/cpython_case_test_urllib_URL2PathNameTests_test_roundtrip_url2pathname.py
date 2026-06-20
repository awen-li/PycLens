# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: URL2PathNameTests_test_roundtrip_url2pathname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    list_of_paths = ['C:', '\\\\\\C\\test\\\\', 'C:\\foo\\bar\\spam.foo']
    for path in list_of_paths:
        self.assertEqual(url2pathname(pathname2url(path)), path)
