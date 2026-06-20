# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ssl.CERT_NONE
    ssl.CERT_OPTIONAL
    ssl.CERT_REQUIRED
    ssl.OP_CIPHER_SERVER_PREFERENCE
    ssl.OP_SINGLE_DH_USE
    ssl.OP_SINGLE_ECDH_USE
    ssl.OP_NO_COMPRESSION
    self.assertEqual(ssl.HAS_SNI, True)
    self.assertEqual(ssl.HAS_ECDH, True)
    self.assertEqual(ssl.HAS_TLSv1_2, True)
    self.assertEqual(ssl.HAS_TLSv1_3, True)
    ssl.OP_NO_SSLv2
    ssl.OP_NO_SSLv3
    ssl.OP_NO_TLSv1
    ssl.OP_NO_TLSv1_3
    ssl.OP_NO_TLSv1_1
    ssl.OP_NO_TLSv1_2
    self.assertEqual(ssl.PROTOCOL_TLS, ssl.PROTOCOL_SSLv23)
