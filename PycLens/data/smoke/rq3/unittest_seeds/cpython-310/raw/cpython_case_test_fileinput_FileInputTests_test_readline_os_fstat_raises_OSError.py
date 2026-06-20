# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_readline_os_fstat_raises_OSError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os_fstat_orig = os.fstat
    os_fstat_replacement = UnconditionallyRaise(OSError)
    try:
        t = self.writeTmp('\n')
        with FileInput(files=[t], inplace=True, encoding='utf-8') as fi:
            os.fstat = os_fstat_replacement
            fi.readline()
    finally:
        os.fstat = os_fstat_orig
    self.assertTrue(os_fstat_replacement.invoked, 'os.fstat() was not invoked')
