# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_ciphers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.set_ciphers('ALL')
    ctx.set_ciphers('DEFAULT')
    with self.assertRaisesRegex(ssl.SSLError, 'No cipher can be selected'):
        ctx.set_ciphers("^$:,;?*'dorothyx")
