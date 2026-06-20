# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelIDTests_test_with_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters._channel_id(10, send=True, force=True)
    self.assertEqual(cid.end, 'send')
    cid = interpreters._channel_id(10, send=True, recv=False, force=True)
    self.assertEqual(cid.end, 'send')
    cid = interpreters._channel_id(10, recv=True, force=True)
    self.assertEqual(cid.end, 'recv')
    cid = interpreters._channel_id(10, recv=True, send=False, force=True)
    self.assertEqual(cid.end, 'recv')
    cid = interpreters._channel_id(10, send=True, recv=True, force=True)
    self.assertEqual(cid.end, 'both')
