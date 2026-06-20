# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: GzipUtilTestCase_test_gzip_decode_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    max_gzip_decode = 20 * 1024 * 1024
    data = b'\x00' * max_gzip_decode
    encoded = xmlrpclib.gzip_encode(data)
    decoded = xmlrpclib.gzip_decode(encoded)
    self.assertEqual(len(decoded), max_gzip_decode)
    data = b'\x00' * (max_gzip_decode + 1)
    encoded = xmlrpclib.gzip_encode(data)
    with self.assertRaisesRegex(ValueError, 'max gzipped payload length exceeded'):
        xmlrpclib.gzip_decode(encoded)
    xmlrpclib.gzip_decode(encoded, max_decode=-1)
