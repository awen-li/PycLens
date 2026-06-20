# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_zip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ans = [(x, y) for (x, y) in zip('abc', count())]
    self.assertEqual(ans, [('a', 0), ('b', 1), ('c', 2)])
    self.assertEqual(list(zip('abc', range(6))), lzip('abc', range(6)))
    self.assertEqual(list(zip('abcdef', range(3))), lzip('abcdef', range(3)))
    self.assertEqual(take(3, zip('abcdef', count())), lzip('abcdef', range(3)))
    self.assertEqual(list(zip('abcdef')), lzip('abcdef'))
    self.assertEqual(list(zip()), lzip())
    self.assertRaises(TypeError, zip, 3)
    self.assertRaises(TypeError, zip, range(3), 3)
    self.assertEqual([tuple(list(pair)) for pair in zip('abc', 'def')], lzip('abc', 'def'))
    self.assertEqual([pair for pair in zip('abc', 'def')], lzip('abc', 'def'))
