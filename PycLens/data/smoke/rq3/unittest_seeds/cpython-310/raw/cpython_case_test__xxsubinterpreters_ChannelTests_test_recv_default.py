# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_recv_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    default = object()
    cid = interpreters.channel_create()
    obj1 = interpreters.channel_recv(cid, default)
    interpreters.channel_send(cid, None)
    interpreters.channel_send(cid, 1)
    interpreters.channel_send(cid, b'spam')
    interpreters.channel_send(cid, b'eggs')
    obj2 = interpreters.channel_recv(cid, default)
    obj3 = interpreters.channel_recv(cid, default)
    obj4 = interpreters.channel_recv(cid)
    obj5 = interpreters.channel_recv(cid, default)
    obj6 = interpreters.channel_recv(cid, default)
    self.assertIs(obj1, default)
    self.assertIs(obj2, None)
    self.assertEqual(obj3, 1)
    self.assertEqual(obj4, b'spam')
    self.assertEqual(obj5, b'eggs')
    self.assertIs(obj6, default)
