# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_uninstantiable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    scandir_iter = os.scandir(self.path)
    self.assertRaises(TypeError, type(scandir_iter))
    scandir_iter.close()
