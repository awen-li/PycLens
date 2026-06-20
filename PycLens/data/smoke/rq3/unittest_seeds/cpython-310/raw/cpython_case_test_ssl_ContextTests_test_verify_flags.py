# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_verify_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    tf = getattr(ssl, 'VERIFY_X509_TRUSTED_FIRST', 0)
    self.assertEqual(ctx.verify_flags, ssl.VERIFY_DEFAULT | tf)
    ctx.verify_flags = ssl.VERIFY_CRL_CHECK_LEAF
    self.assertEqual(ctx.verify_flags, ssl.VERIFY_CRL_CHECK_LEAF)
    ctx.verify_flags = ssl.VERIFY_CRL_CHECK_CHAIN
    self.assertEqual(ctx.verify_flags, ssl.VERIFY_CRL_CHECK_CHAIN)
    ctx.verify_flags = ssl.VERIFY_DEFAULT
    self.assertEqual(ctx.verify_flags, ssl.VERIFY_DEFAULT)
    ctx.verify_flags = ssl.VERIFY_ALLOW_PROXY_CERTS
    self.assertEqual(ctx.verify_flags, ssl.VERIFY_ALLOW_PROXY_CERTS)
    ctx.verify_flags = ssl.VERIFY_CRL_CHECK_LEAF | ssl.VERIFY_X509_STRICT
    self.assertEqual(ctx.verify_flags, ssl.VERIFY_CRL_CHECK_LEAF | ssl.VERIFY_X509_STRICT)
    with self.assertRaises(TypeError):
        ctx.verify_flags = None
