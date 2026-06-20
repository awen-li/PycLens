# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_iterators_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict()
    empty = []
    self.assertEqual(list(od), empty)
    self.assertEqual(list(od.keys()), empty)
    self.assertEqual(list(od.values()), empty)
    self.assertEqual(list(od.items()), empty)
    self.assertEqual(list(reversed(od)), empty)
    self.assertEqual(list(reversed(od.keys())), empty)
    self.assertEqual(list(reversed(od.values())), empty)
    self.assertEqual(list(reversed(od.items())), empty)
