# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: PathLikeTests_test_path_normcase

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_function(self.path.normcase)
    if sys.platform == 'win32':
        self.assertEqual(ntpath.normcase('ΩΩ'), 'ωΩ')
