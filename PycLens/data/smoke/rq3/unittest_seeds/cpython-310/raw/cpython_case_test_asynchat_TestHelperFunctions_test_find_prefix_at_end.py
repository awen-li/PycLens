# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestHelperFunctions_test_find_prefix_at_end

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(asynchat.find_prefix_at_end('qwerty\r', '\r\n'), 1)
    self.assertEqual(asynchat.find_prefix_at_end('qwertydkjf', '\r\n'), 0)
