# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_channel_list_interpreters_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(send_interps, [])
    self.assertEqual(recv_interps, [])
