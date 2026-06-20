# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    equal = self.assertEqual
    for (u, v) in [(self.uuid.uuid3(self.uuid.NAMESPACE_DNS, 'python.org'), '6fa459ea-ee8a-3ca4-894e-db77e160355e'), (self.uuid.uuid3(self.uuid.NAMESPACE_URL, 'http://python.org/'), '9fe8e8c4-aaa8-32a9-a55c-4535a88b748d'), (self.uuid.uuid3(self.uuid.NAMESPACE_OID, '1.3.6.1'), 'dd1a1cef-13d5-368a-ad82-eca71acd4cd1'), (self.uuid.uuid3(self.uuid.NAMESPACE_X500, 'c=ca'), '658d3002-db6b-3040-a1d1-8ddd7d189a4d')]:
        equal(u.variant, self.uuid.RFC_4122)
        equal(u.version, 3)
        equal(u, self.uuid.UUID(v))
        equal(str(u), v)
