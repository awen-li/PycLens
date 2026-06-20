# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_load_verify_locations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_verify_locations(CERTFILE)
    ctx.load_verify_locations(cafile=CERTFILE, capath=None)
    ctx.load_verify_locations(BYTES_CERTFILE)
    ctx.load_verify_locations(cafile=BYTES_CERTFILE, capath=None)
    self.assertRaises(TypeError, ctx.load_verify_locations)
    self.assertRaises(TypeError, ctx.load_verify_locations, None, None, None)
    with self.assertRaises(OSError) as cm:
        ctx.load_verify_locations(NONEXISTINGCERT)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
    with self.assertRaisesRegex(ssl.SSLError, 'PEM lib'):
        ctx.load_verify_locations(BADCERT)
    ctx.load_verify_locations(CERTFILE, CAPATH)
    ctx.load_verify_locations(CERTFILE, capath=BYTES_CAPATH)
    self.assertRaises(TypeError, ctx.load_verify_locations, None, True)
