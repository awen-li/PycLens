# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestInternalUtilities_test_sys_path_adjustment_protects_pydoc_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _get_revised_path(given_path):
        return self._get_revised_path(given_path, argv0=pydoc.__file__)
    clean_path = self._get_starting_path()
    leading_argv0dir = [self.argv0dir] + clean_path
    expected_path = [self.abs_curdir] + leading_argv0dir
    self.assertEqual(_get_revised_path(leading_argv0dir), expected_path)
    trailing_argv0dir = clean_path + [self.argv0dir]
    expected_path = [self.abs_curdir] + trailing_argv0dir
    self.assertEqual(_get_revised_path(trailing_argv0dir), expected_path)
