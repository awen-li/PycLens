# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_get_ciphers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.set_ciphers('AESGCM')
    names = set((d['name'] for d in ctx.get_ciphers()))
    expected = {'AES128-GCM-SHA256', 'ECDHE-ECDSA-AES128-GCM-SHA256', 'ECDHE-RSA-AES128-GCM-SHA256', 'DHE-RSA-AES128-GCM-SHA256', 'AES256-GCM-SHA384', 'ECDHE-ECDSA-AES256-GCM-SHA384', 'ECDHE-RSA-AES256-GCM-SHA384', 'DHE-RSA-AES256-GCM-SHA384'}
    intersection = names.intersection(expected)
    self.assertGreaterEqual(len(intersection), 2, f'\ngot: {sorted(names)}\nexpected: {sorted(expected)}')
