# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_PROTOCOL_TLS

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    if has_tls_version('SSLv2'):
        try:
            try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_SSLv2, True)
        except OSError as x:
            if support.verbose:
                sys.stdout.write(' SSL2 client to SSL23 server test unexpectedly failed:\n %s\n' % str(x))
    if has_tls_version('SSLv3'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_SSLv3, False)
    try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLS, True)
    if has_tls_version('TLSv1'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLSv1, 'TLSv1')
    if has_tls_version('SSLv3'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_SSLv3, False, ssl.CERT_OPTIONAL)
    try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLS, True, ssl.CERT_OPTIONAL)
    if has_tls_version('TLSv1'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLSv1, 'TLSv1', ssl.CERT_OPTIONAL)
    if has_tls_version('SSLv3'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_SSLv3, False, ssl.CERT_REQUIRED)
    try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLS, True, ssl.CERT_REQUIRED)
    if has_tls_version('TLSv1'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLSv1, 'TLSv1', ssl.CERT_REQUIRED)
    if has_tls_version('SSLv3'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_SSLv3, False, server_options=ssl.OP_NO_SSLv3)
    try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLS, True, server_options=ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3)
    if has_tls_version('TLSv1'):
        try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLSv1, False, server_options=ssl.OP_NO_TLSv1)
