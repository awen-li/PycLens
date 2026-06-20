# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_unknown_channel_binding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.create_server(('127.0.0.1', 0))
    c = socket.socket(socket.AF_INET)
    c.connect(s.getsockname())
    with test_wrap_socket(c, do_handshake_on_connect=False) as ss:
        with self.assertRaises(ValueError):
            ss.get_channel_binding('unknown-type')
    s.close()
