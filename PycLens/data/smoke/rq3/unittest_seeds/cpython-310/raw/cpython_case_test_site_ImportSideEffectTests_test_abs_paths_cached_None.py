# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: ImportSideEffectTests_test_abs_paths_cached_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sys.modules['test'].__cached__ = None
    site.abs_paths()
    self.assertIsNone(sys.modules['test'].__cached__)
