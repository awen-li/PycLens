# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_get_server_certificate_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def servername_cb(ssl_sock, server_name, initial_context):
        time.sleep(0.2)
    self.server_context.set_servername_callback(servername_cb)
    with self.assertRaises(socket.timeout):
        ssl.get_server_certificate(self.server_addr, ca_certs=SIGNING_CA, timeout=0.1)
