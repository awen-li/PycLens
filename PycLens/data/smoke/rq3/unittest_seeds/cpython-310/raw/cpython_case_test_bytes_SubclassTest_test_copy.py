# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: SubclassTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = self.type2test(b'abcd')
    a.x = 10
    a.y = self.type2test(b'efgh')
    for copy_method in (copy.copy, copy.deepcopy):
        b = copy_method(a)
        self.assertNotEqual(id(a), id(b))
        self.assertEqual(a, b)
        self.assertEqual(a.x, b.x)
        self.assertEqual(a.y, b.y)
        self.assertEqual(type(a), type(b))
        self.assertEqual(type(a.y), type(b.y))
