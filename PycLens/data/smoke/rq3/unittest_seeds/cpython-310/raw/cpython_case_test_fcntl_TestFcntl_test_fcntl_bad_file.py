# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_fcntl_bad_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        fcntl.fcntl(-1, fcntl.F_SETFL, os.O_NONBLOCK)
    with self.assertRaises(ValueError):
        fcntl.fcntl(BadFile(-1), fcntl.F_SETFL, os.O_NONBLOCK)
    with self.assertRaises(TypeError):
        fcntl.fcntl('spam', fcntl.F_SETFL, os.O_NONBLOCK)
    with self.assertRaises(TypeError):
        fcntl.fcntl(BadFile('spam'), fcntl.F_SETFL, os.O_NONBLOCK)
