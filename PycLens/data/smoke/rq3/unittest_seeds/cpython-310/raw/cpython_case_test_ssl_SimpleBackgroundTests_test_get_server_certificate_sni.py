# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_get_server_certificate_sni

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (host, port) = self.server_addr
    server_names = []

    def servername_cb(ssl_sock, server_name, initial_context):
        server_names.append(server_name)
    self.server_context.set_servername_callback(servername_cb)
    pem = ssl.get_server_certificate((host, port))
    if not pem:
        self.fail('No server certificate on %s:%s!' % (host, port))
    pem = ssl.get_server_certificate((host, port), ca_certs=SIGNING_CA)
    if not pem:
        self.fail('No server certificate on %s:%s!' % (host, port))
    if support.verbose:
        sys.stdout.write('\nVerified certificate for %s:%s is\n%s\n' % (host, port, pem))
    self.assertEqual(server_names, [host, host])
