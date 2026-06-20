# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TermsizeTests_test_does_not_crash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        size = os.get_terminal_size()
    except OSError as e:
        if sys.platform == 'win32' or e.errno in (errno.EINVAL, errno.ENOTTY):
            self.skipTest('failed to query terminal size')
        raise
    self.assertGreaterEqual(size.columns, 0)
    self.assertGreaterEqual(size.lines, 0)
