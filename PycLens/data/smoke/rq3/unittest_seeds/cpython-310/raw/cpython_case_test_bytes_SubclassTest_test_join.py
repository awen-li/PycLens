# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: SubclassTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = self.type2test(b'abcd')
    s2 = self.basetype().join([s1])
    self.assertIsNot(s1, s2)
    self.assertIs(type(s2), self.basetype, type(s2))
    s3 = s1.join([b'abcd'])
    self.assertIs(type(s3), self.basetype)
