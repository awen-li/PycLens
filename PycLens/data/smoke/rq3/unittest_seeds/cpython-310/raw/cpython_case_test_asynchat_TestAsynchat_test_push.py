# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestAsynchat_test_push

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (s, event) = start_echo_server()
    c = echo_client(b'\n', s.port)
    data = b'bytes\n'
    c.push(data)
    c.push(bytearray(data))
    c.push(memoryview(data))
    self.assertRaises(TypeError, c.push, 10)
    self.assertRaises(TypeError, c.push, 'unicode')
    c.push(SERVER_QUIT)
    asyncore.loop(use_poll=self.usepoll, count=300, timeout=0.01)
    threading_helper.join_thread(s)
    self.assertEqual(c.contents, [b'bytes', b'bytes', b'bytes'])
