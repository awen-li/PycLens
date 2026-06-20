# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_DER_to_PEM

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(CAFILE_CACERT, 'r') as f:
        pem = f.read()
    d1 = ssl.PEM_cert_to_DER_cert(pem)
    p2 = ssl.DER_cert_to_PEM_cert(d1)
    d2 = ssl.PEM_cert_to_DER_cert(p2)
    self.assertEqual(d1, d2)
    if not p2.startswith(ssl.PEM_HEADER + '\n'):
        self.fail("DER-to-PEM didn't include correct header:\n%r\n" % p2)
    if not p2.endswith('\n' + ssl.PEM_FOOTER + '\n'):
        self.fail("DER-to-PEM didn't include correct footer:\n%r\n" % p2)
