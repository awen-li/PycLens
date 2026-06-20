# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_default_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = collections.defaultdict(int)
    self.assertEqual(pprint.pformat(d, width=1), "defaultdict(<class 'int'>, {})")
    words = 'the quick brown fox jumped over a lazy dog'.split()
    d = collections.defaultdict(int, zip(words, itertools.count()))
    self.assertEqual(pprint.pformat(d), "defaultdict(<class 'int'>,\n            {'a': 6,\n             'brown': 2,\n             'dog': 8,\n             'fox': 3,\n             'jumped': 4,\n             'lazy': 7,\n             'over': 5,\n             'quick': 1,\n             'the': 0})")
