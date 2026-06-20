# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    default = ssl.OP_ALL | ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3
    default |= OP_NO_COMPRESSION | OP_CIPHER_SERVER_PREFERENCE | OP_SINGLE_DH_USE | OP_SINGLE_ECDH_USE | OP_ENABLE_MIDDLEBOX_COMPAT
    self.assertEqual(default, ctx.options)
    with warnings_helper.check_warnings():
        ctx.options |= ssl.OP_NO_TLSv1
    self.assertEqual(default | ssl.OP_NO_TLSv1, ctx.options)
    with warnings_helper.check_warnings():
        ctx.options = ctx.options & ~ssl.OP_NO_TLSv1
    self.assertEqual(default, ctx.options)
    ctx.options = 0
    self.assertEqual(0, ctx.options & ~ssl.OP_NO_SSLv3)
