# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_channel_list_interpreters_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp0 = interpreters.get_main()
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, 'send')
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(send_interps, [interp0])
    self.assertEqual(recv_interps, [])
    interp1 = interpreters.create()
    _run_output(interp1, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_recv({cid})\n            '))
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(send_interps, [interp0])
    self.assertEqual(recv_interps, [interp1])
