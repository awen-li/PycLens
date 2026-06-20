# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_chainmap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = collections.ChainMap()
    self.assertEqual(pprint.pformat(d, width=1), 'ChainMap({})')
    words = 'the quick brown fox jumped over a lazy dog'.split()
    items = list(zip(words, itertools.count()))
    d = collections.ChainMap(dict(items))
    self.assertEqual(pprint.pformat(d), "ChainMap({'a': 6,\n          'brown': 2,\n          'dog': 8,\n          'fox': 3,\n          'jumped': 4,\n          'lazy': 7,\n          'over': 5,\n          'quick': 1,\n          'the': 0})")
    d = collections.ChainMap(dict(items), collections.OrderedDict(items))
    self.assertEqual(pprint.pformat(d), "ChainMap({'a': 6,\n          'brown': 2,\n          'dog': 8,\n          'fox': 3,\n          'jumped': 4,\n          'lazy': 7,\n          'over': 5,\n          'quick': 1,\n          'the': 0},\n         OrderedDict([('the', 0),\n                      ('quick', 1),\n                      ('brown', 2),\n                      ('fox', 3),\n                      ('jumped', 4),\n                      ('over', 5),\n                      ('a', 6),\n                      ('lazy', 7),\n                      ('dog', 8)]))")
