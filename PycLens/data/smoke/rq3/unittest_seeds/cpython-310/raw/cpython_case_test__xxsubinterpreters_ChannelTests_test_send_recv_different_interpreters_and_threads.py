# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_send_recv_different_interpreters_and_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    id1 = interpreters.create()
    out = None

    def f():
        nonlocal out
        out = _run_output(id1, dedent(f"\n                import time\n                import _xxsubinterpreters as _interpreters\n                while True:\n                    try:\n                        obj = _interpreters.channel_recv({cid})\n                        break\n                    except _interpreters.ChannelEmptyError:\n                        time.sleep(0.1)\n                assert(obj == b'spam')\n                _interpreters.channel_send({cid}, b'eggs')\n                "))
    t = threading.Thread(target=f)
    t.start()
    interpreters.channel_send(cid, b'spam')
    t.join()
    obj = interpreters.channel_recv(cid)
    self.assertEqual(obj, b'eggs')
