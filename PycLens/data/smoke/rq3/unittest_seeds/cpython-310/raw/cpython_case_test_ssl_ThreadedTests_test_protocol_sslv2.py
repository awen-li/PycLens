# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_protocol_sslv2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_SSLv2, True)
    try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_SSLv2, True, ssl.CERT_OPTIONAL)
    try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_SSLv2, True, ssl.CERT_REQUIRED)
    try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_TLS, False)
    if has_tls_version('SSLv3'):
        try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_SSLv3, False)
    try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_TLSv1, False)
    try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_TLS, False, client_options=ssl.OP_NO_SSLv3)
    try_protocol_combo(ssl.PROTOCOL_SSLv2, ssl.PROTOCOL_TLS, False, client_options=ssl.OP_NO_TLSv1)
