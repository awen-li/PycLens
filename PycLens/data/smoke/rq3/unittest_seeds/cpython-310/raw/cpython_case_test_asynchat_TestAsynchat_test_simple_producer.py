# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestAsynchat_test_simple_producer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (s, event) = start_echo_server()
    c = echo_client(b'\n', s.port)
    data = b"hello world\nI'm not dead yet!\n"
    p = asynchat.simple_producer(data + SERVER_QUIT, buffer_size=8)
    c.push_with_producer(p)
    asyncore.loop(use_poll=self.usepoll, count=300, timeout=0.01)
    threading_helper.join_thread(s)
    self.assertEqual(c.contents, [b'hello world', b"I'm not dead yet!"])
