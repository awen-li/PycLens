# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: ImportSideEffectTests_test_no_duplicate_paths

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    site.removeduppaths()
    seen_paths = set()
    for path in sys.path:
        self.assertNotIn(path, seen_paths)
        seen_paths.add(path)
