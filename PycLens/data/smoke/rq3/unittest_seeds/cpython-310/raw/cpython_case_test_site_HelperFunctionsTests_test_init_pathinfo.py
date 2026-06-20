# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_init_pathinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir_set = site._init_pathinfo()
    for entry in [site.makepath(path)[1] for path in sys.path if path and os.path.exists(path)]:
        self.assertIn(entry, dir_set, '%s from sys.path not found in set returned by _init_pathinfo(): %s' % (entry, dir_set))
