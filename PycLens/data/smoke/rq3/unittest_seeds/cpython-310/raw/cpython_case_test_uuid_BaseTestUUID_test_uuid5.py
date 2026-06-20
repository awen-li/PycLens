# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    equal = self.assertEqual
    for (u, v) in [(self.uuid.uuid5(self.uuid.NAMESPACE_DNS, 'python.org'), '886313e1-3b8a-5372-9b90-0c9aee199e5d'), (self.uuid.uuid5(self.uuid.NAMESPACE_URL, 'http://python.org/'), '4c565f0d-3f5a-5890-b41b-20cf47701c5e'), (self.uuid.uuid5(self.uuid.NAMESPACE_OID, '1.3.6.1'), '1447fa61-5277-5fef-a9b3-fbc6e44f4af3'), (self.uuid.uuid5(self.uuid.NAMESPACE_X500, 'c=ca'), 'cc957dd1-a972-5349-98cd-874190002798')]:
        equal(u.variant, self.uuid.RFC_4122)
        equal(u.version, 5)
        equal(u, self.uuid.UUID(v))
        equal(str(u), v)
