# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_makepath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path_parts = ('Beginning', 'End')
    original_dir = os.path.join(*path_parts)
    (abs_dir, norm_dir) = site.makepath(*path_parts)
    self.assertEqual(os.path.abspath(original_dir), abs_dir)
    if original_dir == os.path.normcase(original_dir):
        self.assertEqual(abs_dir, norm_dir)
    else:
        self.assertEqual(os.path.normcase(abs_dir), norm_dir)
