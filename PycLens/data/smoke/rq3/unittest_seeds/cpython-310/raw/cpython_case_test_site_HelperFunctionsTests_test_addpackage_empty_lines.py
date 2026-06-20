# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_addpackage_empty_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (pth_dir, pth_fn) = self.make_pth('\n\n  \n\n')
    known_paths = site.addpackage(pth_dir, pth_fn, set())
    self.assertEqual(known_paths, set())
