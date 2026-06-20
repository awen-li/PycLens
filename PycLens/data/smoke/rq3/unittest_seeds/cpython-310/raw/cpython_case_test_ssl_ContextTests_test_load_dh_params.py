# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_load_dh_params

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_dh_params(DHFILE)
    if os.name != 'nt':
        ctx.load_dh_params(BYTES_DHFILE)
    self.assertRaises(TypeError, ctx.load_dh_params)
    self.assertRaises(TypeError, ctx.load_dh_params, None)
    with self.assertRaises(FileNotFoundError) as cm:
        ctx.load_dh_params(NONEXISTINGCERT)
    self.assertEqual(cm.exception.errno, errno.ENOENT)
    with self.assertRaises(ssl.SSLError) as cm:
        ctx.load_dh_params(CERTFILE)
