# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestInternalUtilities_test_sys_path_adjustment_adds_missing_curdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    clean_path = self._get_starting_path()
    expected_path = [self.abs_curdir] + clean_path
    self.assertEqual(self._get_revised_path(clean_path), expected_path)
