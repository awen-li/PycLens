# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class userdict(dict):
        pass
    mapping = {'x': 1, 'y': 2}
    self.assertEqual(self.mappingproxy(mapping), mapping)
    mapping = userdict(x=1, y=2)
    self.assertEqual(self.mappingproxy(mapping), mapping)
    mapping = collections.ChainMap({'x': 1}, {'y': 2})
    self.assertEqual(self.mappingproxy(mapping), mapping)
    self.assertRaises(TypeError, self.mappingproxy, 10)
    self.assertRaises(TypeError, self.mappingproxy, ('a', 'tuple'))
    self.assertRaises(TypeError, self.mappingproxy, ['a', 'list'])
