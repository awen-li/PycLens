# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkdtemp_test_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = self.do_create()
    try:
        mode = stat.S_IMODE(os.stat(dir).st_mode)
        mode &= 511
        expected = 448
        if sys.platform == 'win32':
            user = expected >> 6
            expected = user * (1 + 8 + 64)
        self.assertEqual(mode, expected)
    finally:
        os.rmdir(dir)
