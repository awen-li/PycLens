# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestPEP519_test_fsencode_fsdecode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for p in ('path/like/object', b'path/like/object'):
        pathlike = FakePath(p)
        self.assertEqual(p, self.fspath(pathlike))
        self.assertEqual(b'path/like/object', os.fsencode(pathlike))
        self.assertEqual('path/like/object', os.fsdecode(pathlike))
