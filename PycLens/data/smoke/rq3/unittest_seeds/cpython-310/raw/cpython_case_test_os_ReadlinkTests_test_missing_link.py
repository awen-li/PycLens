# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ReadlinkTests_test_missing_link

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(FileNotFoundError, os.readlink, 'missing-link')
    self.assertRaises(FileNotFoundError, os.readlink, FakePath('missing-link'))
