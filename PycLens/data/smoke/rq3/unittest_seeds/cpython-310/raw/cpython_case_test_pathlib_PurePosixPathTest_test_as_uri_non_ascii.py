# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PurePosixPathTest_test_as_uri_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from urllib.parse import quote_from_bytes
    P = self.cls
    try:
        os.fsencode('é')
    except UnicodeEncodeError:
        self.skipTest('\\xe9 cannot be encoded to the filesystem encoding')
    self.assertEqual(P('/a/bé').as_uri(), 'file:///a/b' + quote_from_bytes(os.fsencode('é')))
