# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestAsynchat_test_none_terminator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (s, event) = start_echo_server()
    c = echo_client(None, s.port)
    data = b"hello world, I'm not dead yet!\n"
    c.push(data)
    c.push(SERVER_QUIT)
    asyncore.loop(use_poll=self.usepoll, count=300, timeout=0.01)
    threading_helper.join_thread(s)
    self.assertEqual(c.contents, [])
    self.assertEqual(c.buffer, data)
