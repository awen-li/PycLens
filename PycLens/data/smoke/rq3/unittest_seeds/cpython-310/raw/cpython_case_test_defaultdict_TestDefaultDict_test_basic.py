# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = defaultdict()
    self.assertEqual(d1.default_factory, None)
    d1.default_factory = list
    d1[12].append(42)
    self.assertEqual(d1, {12: [42]})
    d1[12].append(24)
    self.assertEqual(d1, {12: [42, 24]})
    d1[13]
    d1[14]
    self.assertEqual(d1, {12: [42, 24], 13: [], 14: []})
    self.assertTrue(d1[12] is not d1[13] is not d1[14])
    d2 = defaultdict(list, foo=1, bar=2)
    self.assertEqual(d2.default_factory, list)
    self.assertEqual(d2, {'foo': 1, 'bar': 2})
    self.assertEqual(d2['foo'], 1)
    self.assertEqual(d2['bar'], 2)
    self.assertEqual(d2[42], [])
    self.assertIn('foo', d2)
    self.assertIn('foo', d2.keys())
    self.assertIn('bar', d2)
    self.assertIn('bar', d2.keys())
    self.assertIn(42, d2)
    self.assertIn(42, d2.keys())
    self.assertNotIn(12, d2)
    self.assertNotIn(12, d2.keys())
    d2.default_factory = None
    self.assertEqual(d2.default_factory, None)
    try:
        d2[15]
    except KeyError as err:
        self.assertEqual(err.args, (15,))
    else:
        self.fail("d2[15] didn't raise KeyError")
    self.assertRaises(TypeError, defaultdict, 1)
