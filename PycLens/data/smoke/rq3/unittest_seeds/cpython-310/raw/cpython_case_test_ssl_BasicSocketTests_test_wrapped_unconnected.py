# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_wrapped_unconnected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket(socket.AF_INET)
    with test_wrap_socket(s) as ss:
        self.assertRaises(OSError, ss.recv, 1)
        self.assertRaises(OSError, ss.recv_into, bytearray(b'x'))
        self.assertRaises(OSError, ss.recvfrom, 1)
        self.assertRaises(OSError, ss.recvfrom_into, bytearray(b'x'), 1)
        self.assertRaises(OSError, ss.send, b'x')
        self.assertRaises(OSError, ss.sendto, b'x', ('0.0.0.0', 0))
        self.assertRaises(NotImplementedError, ss.dup)
        self.assertRaises(NotImplementedError, ss.sendmsg, [b'x'], (), 0, ('0.0.0.0', 0))
        self.assertRaises(NotImplementedError, ss.recvmsg, 100)
        self.assertRaises(NotImplementedError, ss.recvmsg_into, [bytearray(100)])
