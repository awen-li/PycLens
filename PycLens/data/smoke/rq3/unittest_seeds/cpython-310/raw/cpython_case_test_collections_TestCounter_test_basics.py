# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = Counter('abcaba')
    self.assertEqual(c, Counter({'a': 3, 'b': 2, 'c': 1}))
    self.assertEqual(c, Counter(a=3, b=2, c=1))
    self.assertIsInstance(c, dict)
    self.assertIsInstance(c, Mapping)
    self.assertTrue(issubclass(Counter, dict))
    self.assertTrue(issubclass(Counter, Mapping))
    self.assertEqual(len(c), 3)
    self.assertEqual(sum(c.values()), 6)
    self.assertEqual(list(c.values()), [3, 2, 1])
    self.assertEqual(list(c.keys()), ['a', 'b', 'c'])
    self.assertEqual(list(c), ['a', 'b', 'c'])
    self.assertEqual(list(c.items()), [('a', 3), ('b', 2), ('c', 1)])
    self.assertEqual(c['b'], 2)
    self.assertEqual(c['z'], 0)
    self.assertEqual(c.__contains__('c'), True)
    self.assertEqual(c.__contains__('z'), False)
    self.assertEqual(c.get('b', 10), 2)
    self.assertEqual(c.get('z', 10), 10)
    self.assertEqual(c, dict(a=3, b=2, c=1))
    self.assertEqual(repr(c), "Counter({'a': 3, 'b': 2, 'c': 1})")
    self.assertEqual(c.most_common(), [('a', 3), ('b', 2), ('c', 1)])
    for i in range(5):
        self.assertEqual(c.most_common(i), [('a', 3), ('b', 2), ('c', 1)][:i])
    self.assertEqual(''.join(c.elements()), 'aaabbc')
    c['a'] += 1
    c['b'] -= 2
    del c['c']
    del c['c']
    c['d'] -= 2
    c['e'] = -5
    c['f'] += 4
    self.assertEqual(c, dict(a=4, b=0, d=-2, e=-5, f=4))
    self.assertEqual(''.join(c.elements()), 'aaaaffff')
    self.assertEqual(c.pop('f'), 4)
    self.assertNotIn('f', c)
    for i in range(3):
        (elem, cnt) = c.popitem()
        self.assertNotIn(elem, c)
    c.clear()
    self.assertEqual(c, {})
    self.assertEqual(repr(c), 'Counter()')
    self.assertRaises(NotImplementedError, Counter.fromkeys, 'abc')
    self.assertRaises(TypeError, hash, c)
    c.update(dict(a=5, b=3))
    c.update(c=1)
    c.update(Counter('a' * 50 + 'b' * 30))
    c.update()
    c.__init__('a' * 500 + 'b' * 300)
    c.__init__('cdc')
    c.__init__()
    self.assertEqual(c, dict(a=555, b=333, c=3, d=1))
    self.assertEqual(c.setdefault('d', 5), 1)
    self.assertEqual(c['d'], 1)
    self.assertEqual(c.setdefault('e', 5), 5)
    self.assertEqual(c['e'], 5)
