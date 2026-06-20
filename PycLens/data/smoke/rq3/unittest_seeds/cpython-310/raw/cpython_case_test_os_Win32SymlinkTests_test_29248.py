# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32SymlinkTests_test_29248

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    target = os.readlink('C:\\Users\\All Users')
    self.assertTrue(os.path.samefile(target, 'C:\\ProgramData'))
