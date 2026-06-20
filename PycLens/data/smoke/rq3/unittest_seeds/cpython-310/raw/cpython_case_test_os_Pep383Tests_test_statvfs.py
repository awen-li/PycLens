# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Pep383Tests_test_statvfs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fn in self.unicodefn:
        fullname = os.path.join(self.dir, fn)
        os.statvfs(fullname)
