# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SSLErrorTests_test_bad_server_hostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.create_default_context()
    with self.assertRaises(ValueError):
        ctx.wrap_bio(ssl.MemoryBIO(), ssl.MemoryBIO(), server_hostname='')
    with self.assertRaises(ValueError):
        ctx.wrap_bio(ssl.MemoryBIO(), ssl.MemoryBIO(), server_hostname='.example.org')
    with self.assertRaises(TypeError):
        ctx.wrap_bio(ssl.MemoryBIO(), ssl.MemoryBIO(), server_hostname='example.org\x00evil.com')
