# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestNamedTemporaryFile_test_creates_named

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tempfile.NamedTemporaryFile()
    self.assertTrue(os.path.exists(f.name), 'NamedTemporaryFile %s does not exist' % f.name)
