# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_tls_unique_channel_binding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket(socket.AF_INET)
    with test_wrap_socket(s) as ss:
        self.assertIsNone(ss.get_channel_binding('tls-unique'))
    s = socket.socket(socket.AF_INET)
    with test_wrap_socket(s, server_side=True, certfile=CERTFILE) as ss:
        self.assertIsNone(ss.get_channel_binding('tls-unique'))
