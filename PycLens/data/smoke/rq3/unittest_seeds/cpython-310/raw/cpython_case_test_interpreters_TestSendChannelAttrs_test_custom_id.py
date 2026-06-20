# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendChannelAttrs_test_custom_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sch = interpreters.SendChannel(1)
    self.assertEqual(sch.id, 1)
    with self.assertRaises(TypeError):
        interpreters.SendChannel('1')
