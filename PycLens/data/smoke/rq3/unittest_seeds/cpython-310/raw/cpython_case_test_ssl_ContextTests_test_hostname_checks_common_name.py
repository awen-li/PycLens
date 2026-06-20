# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_hostname_checks_common_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertTrue(ctx.hostname_checks_common_name)
    if ssl.HAS_NEVER_CHECK_COMMON_NAME:
        ctx.hostname_checks_common_name = True
        self.assertTrue(ctx.hostname_checks_common_name)
        ctx.hostname_checks_common_name = False
        self.assertFalse(ctx.hostname_checks_common_name)
        ctx.hostname_checks_common_name = True
        self.assertTrue(ctx.hostname_checks_common_name)
    else:
        with self.assertRaises(AttributeError):
            ctx.hostname_checks_common_name = True
