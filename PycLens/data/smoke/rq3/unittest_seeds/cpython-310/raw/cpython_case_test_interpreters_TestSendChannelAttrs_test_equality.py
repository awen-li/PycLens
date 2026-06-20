# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendChannelAttrs_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (_, ch1) = interpreters.create_channel()
    (_, ch2) = interpreters.create_channel()
    self.assertEqual(ch1, ch1)
    self.assertNotEqual(ch1, ch2)
