# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_protocol_tlsv1_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    try_protocol_combo(ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_TLSv1_2, 'TLSv1.2', server_options=ssl.OP_NO_SSLv3 | ssl.OP_NO_SSLv2, client_options=ssl.OP_NO_SSLv3 | ssl.OP_NO_SSLv2)
    if has_tls_version('SSLv2'):
        try_protocol_combo(ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_SSLv2, False)
    if has_tls_version('SSLv3'):
        try_protocol_combo(ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_SSLv3, False)
    try_protocol_combo(ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_TLS, False, client_options=ssl.OP_NO_TLSv1_2)
    try_protocol_combo(ssl.PROTOCOL_TLS, ssl.PROTOCOL_TLSv1_2, 'TLSv1.2')
    if has_tls_protocol(ssl.PROTOCOL_TLSv1):
        try_protocol_combo(ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_TLSv1, False)
        try_protocol_combo(ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_2, False)
    if has_tls_protocol(ssl.PROTOCOL_TLSv1_1):
        try_protocol_combo(ssl.PROTOCOL_TLSv1_2, ssl.PROTOCOL_TLSv1_1, False)
        try_protocol_combo(ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2, False)
