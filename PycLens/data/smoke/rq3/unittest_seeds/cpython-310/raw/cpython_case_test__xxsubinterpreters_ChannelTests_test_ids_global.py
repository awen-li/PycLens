# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_ids_global

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    id1 = interpreters.create()
    out = _run_output(id1, dedent('\n            import _xxsubinterpreters as _interpreters\n            cid = _interpreters.channel_create()\n            print(cid)\n            '))
    cid1 = int(out.strip())
    id2 = interpreters.create()
    out = _run_output(id2, dedent('\n            import _xxsubinterpreters as _interpreters\n            cid = _interpreters.channel_create()\n            print(cid)\n            '))
    cid2 = int(out.strip())
    self.assertEqual(cid2, int(cid1) + 1)
