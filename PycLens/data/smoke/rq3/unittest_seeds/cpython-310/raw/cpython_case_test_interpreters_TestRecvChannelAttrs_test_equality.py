# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestRecvChannelAttrs_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (ch1, _) = interpreters.create_channel()
    (ch2, _) = interpreters.create_channel()
    self.assertEqual(ch1, ch1)
    self.assertNotEqual(ch1, ch2)
