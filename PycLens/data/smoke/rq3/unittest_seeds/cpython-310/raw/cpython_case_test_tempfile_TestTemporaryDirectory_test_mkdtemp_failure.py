# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_mkdtemp_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryDirectory() as nonexistent:
        pass
    with self.assertRaises(FileNotFoundError) as cm:
        tempfile.TemporaryDirectory(dir=nonexistent)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
