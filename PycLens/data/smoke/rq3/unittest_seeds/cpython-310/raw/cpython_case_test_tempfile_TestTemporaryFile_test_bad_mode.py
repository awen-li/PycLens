# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryFile_test_bad_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    self.addCleanup(os_helper.rmtree, dir)
    with self.assertRaises(ValueError):
        tempfile.TemporaryFile(mode='wr', dir=dir)
    with self.assertRaises(TypeError):
        tempfile.TemporaryFile(mode=2, dir=dir)
    self.assertEqual(os.listdir(dir), [])
