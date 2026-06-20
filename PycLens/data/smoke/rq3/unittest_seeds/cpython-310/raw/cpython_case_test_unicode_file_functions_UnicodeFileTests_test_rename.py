# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_file_functions.py
# case: UnicodeFileTests_test_rename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in self.files:
        os.rename(name, 'tmp')
        os.rename('tmp', name)
