# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_ordered_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = collections.OrderedDict()
    self.assertEqual(pprint.pformat(d, width=1), 'OrderedDict()')
    d = collections.OrderedDict([])
    self.assertEqual(pprint.pformat(d, width=1), 'OrderedDict()')
    words = 'the quick brown fox jumped over a lazy dog'.split()
    d = collections.OrderedDict(zip(words, itertools.count()))
    self.assertEqual(pprint.pformat(d), "OrderedDict([('the', 0),\n             ('quick', 1),\n             ('brown', 2),\n             ('fox', 3),\n             ('jumped', 4),\n             ('over', 5),\n             ('a', 6),\n             ('lazy', 7),\n             ('dog', 8)])")
