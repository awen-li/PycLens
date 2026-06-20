# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryFile_test_bad_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    self.addCleanup(os_helper.rmtree, dir)
    with self.assertRaises(LookupError):
        tempfile.TemporaryFile('w', encoding='bad-encoding', dir=dir)
    self.assertEqual(os.listdir(dir), [])
