# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_link

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.symlink(os.getcwd(), TESTFN)
    except (OSError, NotImplementedError) as err:
        raise unittest.SkipTest(str(err))
    else:
        (st_mode, modestr) = self.get_mode()
        self.assertEqual(modestr[0], 'l')
        self.assertS_IS('LNK', st_mode)
