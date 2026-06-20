# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_stat.py
# case: TestFilemode_test_socket

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket(socket.AF_UNIX) as s:
        s.bind(TESTFN)
        (st_mode, modestr) = self.get_mode()
        self.assertEqual(modestr[0], 's')
        self.assertS_IS('SOCK', st_mode)
