# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = ChainMap()
    c['a'] = 1
    c['b'] = 2
    d = c.new_child()
    d['b'] = 20
    d['c'] = 30
    self.assertEqual(d.maps, [{'b': 20, 'c': 30}, {'a': 1, 'b': 2}])
    self.assertEqual(d.items(), dict(a=1, b=20, c=30).items())
    self.assertEqual(len(d), 3)
    for key in 'abc':
        self.assertIn(key, d)
    for (k, v) in dict(a=1, b=20, c=30, z=100).items():
        self.assertEqual(d.get(k, 100), v)
    del d['b']
    self.assertEqual(d.maps, [{'c': 30}, {'a': 1, 'b': 2}])
    self.assertEqual(d.items(), dict(a=1, b=2, c=30).items())
    self.assertEqual(len(d), 3)
    for key in 'abc':
        self.assertIn(key, d)
    for (k, v) in dict(a=1, b=2, c=30, z=100).items():
        self.assertEqual(d.get(k, 100), v)
    self.assertIn(repr(d), [type(d).__name__ + "({'c': 30}, {'a': 1, 'b': 2})", type(d).__name__ + "({'c': 30}, {'b': 2, 'a': 1})"])
    for e in (d.copy(), copy.copy(d)):
        self.assertEqual(d, e)
        self.assertEqual(d.maps, e.maps)
        self.assertIsNot(d, e)
        self.assertIsNot(d.maps[0], e.maps[0])
        for (m1, m2) in zip(d.maps[1:], e.maps[1:]):
            self.assertIs(m1, m2)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        e = pickle.loads(pickle.dumps(d, proto))
        self.assertEqual(d, e)
        self.assertEqual(d.maps, e.maps)
        self.assertIsNot(d, e)
        for (m1, m2) in zip(d.maps, e.maps):
            self.assertIsNot(m1, m2, e)
    for e in [copy.deepcopy(d), eval(repr(d))]:
        self.assertEqual(d, e)
        self.assertEqual(d.maps, e.maps)
        self.assertIsNot(d, e)
        for (m1, m2) in zip(d.maps, e.maps):
            self.assertIsNot(m1, m2, e)
    f = d.new_child()
    f['b'] = 5
    self.assertEqual(f.maps, [{'b': 5}, {'c': 30}, {'a': 1, 'b': 2}])
    self.assertEqual(f.parents.maps, [{'c': 30}, {'a': 1, 'b': 2}])
    self.assertEqual(f['b'], 5)
    self.assertEqual(f.parents['b'], 2)
