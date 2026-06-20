# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelReleaseTests_test_multiple_users

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    id1 = interpreters.create()
    id2 = interpreters.create()
    interpreters.run_string(id1, dedent(f"\n            import _xxsubinterpreters as _interpreters\n            _interpreters.channel_send({cid}, b'spam')\n            "))
    out = _run_output(id2, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_recv({cid})\n            _interpreters.channel_release({cid})\n            print(repr(obj))\n            '))
    interpreters.run_string(id1, dedent(f'\n            _interpreters.channel_release({cid})\n            '))
    self.assertEqual(out.strip(), "b'spam'")
