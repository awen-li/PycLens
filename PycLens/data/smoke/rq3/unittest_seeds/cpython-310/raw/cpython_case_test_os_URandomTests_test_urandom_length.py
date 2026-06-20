# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: URandomTests_test_urandom_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(len(os.urandom(0)), 0)
    self.assertEqual(len(os.urandom(1)), 1)
    self.assertEqual(len(os.urandom(10)), 10)
    self.assertEqual(len(os.urandom(100)), 100)
    self.assertEqual(len(os.urandom(1000)), 1000)
