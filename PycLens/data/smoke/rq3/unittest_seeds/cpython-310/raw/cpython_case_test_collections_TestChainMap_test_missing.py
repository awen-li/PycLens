# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DefaultChainMap(ChainMap):

        def __missing__(self, key):
            return 999
    d = DefaultChainMap(dict(a=1, b=2), dict(b=20, c=30))
    for (k, v) in dict(a=1, b=2, c=30, d=999).items():
        self.assertEqual(d[k], v)
    for (k, v) in dict(a=1, b=2, c=30, d=77).items():
        self.assertEqual(d.get(k, 77), v)
    for (k, v) in dict(a=True, b=True, c=True, d=False).items():
        self.assertEqual(k in d, v)
    self.assertEqual(d.pop('a', 1001), 1, d)
    self.assertEqual(d.pop('a', 1002), 1002)
    self.assertEqual(d.popitem(), ('b', 2))
    with self.assertRaises(KeyError):
        d.popitem()
