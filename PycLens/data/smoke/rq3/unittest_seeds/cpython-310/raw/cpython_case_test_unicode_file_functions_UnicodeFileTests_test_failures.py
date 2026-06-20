# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_file_functions.py
# case: UnicodeFileTests_test_failures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in self.files:
        name = 'not_' + name
        self._apply_failure(open, name)
        self._apply_failure(os.stat, name)
        self._apply_failure(os.chdir, name)
        self._apply_failure(os.rmdir, name)
        self._apply_failure(os.remove, name)
        self._apply_failure(os.listdir, name)
