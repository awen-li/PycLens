# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_mapping_proxy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    words = 'the quick brown fox jumped over a lazy dog'.split()
    d = dict(zip(words, itertools.count()))
    m = types.MappingProxyType(d)
    self.assertEqual(pprint.pformat(m), "mappingproxy({'a': 6,\n              'brown': 2,\n              'dog': 8,\n              'fox': 3,\n              'jumped': 4,\n              'lazy': 7,\n              'over': 5,\n              'quick': 1,\n              'the': 0})")
    d = collections.OrderedDict(zip(words, itertools.count()))
    m = types.MappingProxyType(d)
    self.assertEqual(pprint.pformat(m), "mappingproxy(OrderedDict([('the', 0),\n                          ('quick', 1),\n                          ('brown', 2),\n                          ('fox', 3),\n                          ('jumped', 4),\n                          ('over', 5),\n                          ('a', 6),\n                          ('lazy', 7),\n                          ('dog', 8)]))")
