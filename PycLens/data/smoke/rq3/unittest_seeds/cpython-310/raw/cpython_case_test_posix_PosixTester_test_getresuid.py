# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_getresuid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    user_ids = posix.getresuid()
    self.assertEqual(len(user_ids), 3)
    for val in user_ids:
        self.assertGreaterEqual(val, 0)
