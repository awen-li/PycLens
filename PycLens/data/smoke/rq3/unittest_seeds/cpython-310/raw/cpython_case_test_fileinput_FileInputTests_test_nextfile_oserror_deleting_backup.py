# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_nextfile_oserror_deleting_backup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os_unlink_orig = os.unlink
    os_unlink_replacement = UnconditionallyRaise(OSError)
    try:
        t = self.writeTmp('\n')
        self.addCleanup(safe_unlink, t + '.bak')
        with FileInput(files=[t], inplace=True, encoding='utf-8') as fi:
            next(fi)
            os.unlink = os_unlink_replacement
            fi.nextfile()
    finally:
        os.unlink = os_unlink_orig
    self.assertTrue(os_unlink_replacement.invoked, 'os.unlink() was not invoked')
