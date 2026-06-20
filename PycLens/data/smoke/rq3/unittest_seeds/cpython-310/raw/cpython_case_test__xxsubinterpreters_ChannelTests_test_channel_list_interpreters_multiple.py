# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_channel_list_interpreters_multiple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp0 = interpreters.get_main()
    interp1 = interpreters.create()
    interp2 = interpreters.create()
    interp3 = interpreters.create()
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, 'send')
    _run_output(interp1, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            _interpreters.channel_send({cid}, "send")\n            '))
    _run_output(interp2, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_recv({cid})\n            '))
    _run_output(interp3, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_recv({cid})\n            '))
    send_interps = interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = interpreters.channel_list_interpreters(cid, send=False)
    self.assertEqual(set(send_interps), {interp0, interp1})
    self.assertEqual(set(recv_interps), {interp2, interp3})
