# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: SubclassTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(self.type2test, self.basetype))
    self.assertIsInstance(self.type2test(), self.basetype)
    (a, b) = (b'abcd', b'efgh')
    (_a, _b) = (self.type2test(a), self.type2test(b))
    self.assertTrue(_a == _a)
    self.assertTrue(_a != _b)
    self.assertTrue(_a < _b)
    self.assertTrue(_a <= _b)
    self.assertTrue(_b >= _a)
    self.assertTrue(_b > _a)
    self.assertIsNot(_a, a)
    self.assertEqual(a + b, _a + _b)
    self.assertEqual(a + b, a + _b)
    self.assertEqual(a + b, _a + b)
    self.assertTrue(a * 5 == _a * 5)
