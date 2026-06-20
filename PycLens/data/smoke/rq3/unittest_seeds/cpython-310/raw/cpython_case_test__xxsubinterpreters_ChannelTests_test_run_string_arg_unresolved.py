# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_run_string_arg_unresolved

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interp = interpreters.create()
    out = _run_output(interp, dedent("\n            import _xxsubinterpreters as _interpreters\n            print(cid.end)\n            _interpreters.channel_send(cid, b'spam')\n            "), dict(cid=cid.send))
    obj = interpreters.channel_recv(cid)
    self.assertEqual(obj, b'spam')
    self.assertEqual(out.strip(), 'send')
