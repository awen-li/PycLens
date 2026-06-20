# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_send_recv_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    orig = b'spam'
    interpreters.channel_send(cid, orig)
    obj = interpreters.channel_recv(cid)
    self.assertEqual(obj, orig)
    self.assertIsNot(obj, orig)
