# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_channel_list_interpreters_released

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp0 = interpreters.get_main()
    interp1 = interpreters.create()
    interp2 = interpreters.create()
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, 'data')
    _run_output(interp1, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_recv({cid})\n            '))
    interpreters.channel_send(cid, 'data')
    _run_output(interp2, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_recv({cid})\n            '))
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(len(send_interps), 1)
    self.assertEqual(len(recv_interps), 2)
    interpreters.channel_release(cid, send=True)
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(len(send_interps), 0)
    self.assertEqual(len(recv_interps), 2)
    _run_output(interp2, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            _interpreters.channel_release({cid})\n            '))
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(len(send_interps), 0)
    self.assertEqual(recv_interps, [interp1])
