# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilTests_test_unreadable_dir_on_syspath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    package_name = 'unreadable_package'
    d = os.path.join(self.dirname, package_name)
    os.mkdir(d, 0)
    self.addCleanup(os.rmdir, d)
    for t in pkgutil.walk_packages(path=[self.dirname]):
        self.fail('unexpected package found')
