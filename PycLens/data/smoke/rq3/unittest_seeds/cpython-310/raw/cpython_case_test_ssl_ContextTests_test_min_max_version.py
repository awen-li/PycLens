# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_min_max_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    minimum_range = {ssl.TLSVersion.MINIMUM_SUPPORTED, ssl.TLSVersion.TLSv1, ssl.TLSVersion.TLSv1_2}
    maximum_range = {ssl.TLSVersion.MAXIMUM_SUPPORTED, ssl.TLSVersion.TLSv1_3}
    self.assertIn(ctx.minimum_version, minimum_range)
    self.assertIn(ctx.maximum_version, maximum_range)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_1
    ctx.maximum_version = ssl.TLSVersion.TLSv1_2
    self.assertEqual(ctx.minimum_version, ssl.TLSVersion.TLSv1_1)
    self.assertEqual(ctx.maximum_version, ssl.TLSVersion.TLSv1_2)
    ctx.minimum_version = ssl.TLSVersion.MINIMUM_SUPPORTED
    ctx.maximum_version = ssl.TLSVersion.TLSv1
    self.assertEqual(ctx.minimum_version, ssl.TLSVersion.MINIMUM_SUPPORTED)
    self.assertEqual(ctx.maximum_version, ssl.TLSVersion.TLSv1)
    ctx.maximum_version = ssl.TLSVersion.MAXIMUM_SUPPORTED
    self.assertEqual(ctx.maximum_version, ssl.TLSVersion.MAXIMUM_SUPPORTED)
    ctx.maximum_version = ssl.TLSVersion.MINIMUM_SUPPORTED
    self.assertIn(ctx.maximum_version, {ssl.TLSVersion.TLSv1, ssl.TLSVersion.TLSv1_1, ssl.TLSVersion.SSLv3})
    ctx.minimum_version = ssl.TLSVersion.MAXIMUM_SUPPORTED
    self.assertIn(ctx.minimum_version, {ssl.TLSVersion.TLSv1_2, ssl.TLSVersion.TLSv1_3})
    with self.assertRaises(ValueError):
        ctx.minimum_version = 42
    if has_tls_protocol(ssl.PROTOCOL_TLSv1_1):
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
        self.assertIn(ctx.minimum_version, minimum_range)
        self.assertEqual(ctx.maximum_version, ssl.TLSVersion.MAXIMUM_SUPPORTED)
        with self.assertRaises(ValueError):
            ctx.minimum_version = ssl.TLSVersion.MINIMUM_SUPPORTED
        with self.assertRaises(ValueError):
            ctx.maximum_version = ssl.TLSVersion.TLSv1
