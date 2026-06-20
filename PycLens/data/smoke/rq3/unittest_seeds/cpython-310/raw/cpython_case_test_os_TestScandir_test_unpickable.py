# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_unpickable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = self.create_file('file.txt')
    scandir_iter = os.scandir(self.path)
    import pickle
    self.assertRaises(TypeError, pickle.dumps, scandir_iter, filename)
    scandir_iter.close()
