# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.mkdir(TESTFN)
    os.chmod(TESTFN, 448)
    (st_mode, modestr) = self.get_mode()
    self.assertS_IS('DIR', st_mode)
    if os.name == 'posix':
        self.assertEqual(modestr, 'drwx------')
    else:
        self.assertEqual(modestr[0], 'd')
