# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_channel_list_interpreters_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp0 = interpreters.get_main()
    interp1 = interpreters.create()
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, 'send')
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(len(send_interps), 1)
    self.assertEqual(len(recv_interps), 0)
    interpreters.channel_close(cid, force=True)
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_list_interpreters(cid, send=True)
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_list_interpreters(cid, send=False)
