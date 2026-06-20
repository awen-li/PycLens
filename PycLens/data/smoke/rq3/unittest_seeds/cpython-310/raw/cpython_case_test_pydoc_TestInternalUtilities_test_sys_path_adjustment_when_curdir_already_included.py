# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestInternalUtilities_test_sys_path_adjustment_when_curdir_already_included

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    clean_path = self._get_starting_path()
    for spelling in self.curdir_spellings:
        with self.subTest(curdir_spelling=spelling):
            leading_curdir = [spelling] + clean_path
            self.assertIsNone(self._get_revised_path(leading_curdir))
            trailing_curdir = clean_path + [spelling]
            self.assertIsNone(self._get_revised_path(trailing_curdir))
            leading_argv0dir = [self.argv0dir] + leading_curdir
            self.assertIsNone(self._get_revised_path(leading_argv0dir))
            trailing_argv0dir = trailing_curdir + [self.argv0dir]
            self.assertIsNone(self._get_revised_path(trailing_argv0dir))
