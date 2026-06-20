# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_new_child

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = ChainMap()
    c['a'] = 1
    c['b'] = 2
    m = {'b': 20, 'c': 30}
    d = c.new_child(m)
    self.assertEqual(d.maps, [{'b': 20, 'c': 30}, {'a': 1, 'b': 2}])
    self.assertIs(m, d.maps[0])

    class lowerdict(dict):

        def __getitem__(self, key):
            if isinstance(key, str):
                key = key.lower()
            return dict.__getitem__(self, key)

        def __contains__(self, key):
            if isinstance(key, str):
                key = key.lower()
            return dict.__contains__(self, key)
    c = ChainMap()
    c['a'] = 1
    c['b'] = 2
    m = lowerdict(b=20, c=30)
    d = c.new_child(m)
    self.assertIs(m, d.maps[0])
    for key in 'abc':
        self.assertIn(key, d)
    for (k, v) in dict(a=1, B=20, C=30, z=100).items():
        self.assertEqual(d.get(k, 100), v)
    c = ChainMap({'a': 1, 'b': 2})
    d = c.new_child(b=20, c=30)
    self.assertEqual(d.maps, [{'b': 20, 'c': 30}, {'a': 1, 'b': 2}])
