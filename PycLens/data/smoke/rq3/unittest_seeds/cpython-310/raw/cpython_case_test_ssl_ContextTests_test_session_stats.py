# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_session_stats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in {ssl.PROTOCOL_TLS_CLIENT, ssl.PROTOCOL_TLS_SERVER}:
        ctx = ssl.SSLContext(proto)
        self.assertEqual(ctx.session_stats(), {'number': 0, 'connect': 0, 'connect_good': 0, 'connect_renegotiate': 0, 'accept': 0, 'accept_good': 0, 'accept_renegotiate': 0, 'hits': 0, 'misses': 0, 'timeouts': 0, 'cache_full': 0})
