# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelIDTests_test_bad_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, interpreters._channel_id, object())
    self.assertRaises(TypeError, interpreters._channel_id, 10.0)
    self.assertRaises(TypeError, interpreters._channel_id, '10')
    self.assertRaises(TypeError, interpreters._channel_id, b'10')
    self.assertRaises(ValueError, interpreters._channel_id, -1)
    self.assertRaises(OverflowError, interpreters._channel_id, 2 ** 64)
