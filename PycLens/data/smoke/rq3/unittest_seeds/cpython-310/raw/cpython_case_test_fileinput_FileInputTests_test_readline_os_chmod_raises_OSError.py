# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_readline_os_chmod_raises_OSError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os_chmod_orig = os.chmod
    os_chmod_replacement = UnconditionallyRaise(OSError)
    try:
        t = self.writeTmp('\n')
        with FileInput(files=[t], inplace=True, encoding='utf-8') as fi:
            os.chmod = os_chmod_replacement
            fi.readline()
    finally:
        os.chmod = os_chmod_orig
    self.assertTrue(os_chmod_replacement.invoked, 'os.fstat() was not invoked')
