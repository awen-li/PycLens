# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestScandir_test_resource_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.create_file('file.txt')
    self.create_file('file2.txt')
    iterator = os.scandir(self.path)
    next(iterator)
    with self.assertWarns(ResourceWarning):
        del iterator
        support.gc_collect()
    iterator = os.scandir(self.path)
    list(iterator)
    with self.check_no_resource_warning():
        del iterator
