# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_iterators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    shuffle(pairs)
    od = OrderedDict(pairs)
    self.assertEqual(list(od), [t[0] for t in pairs])
    self.assertEqual(list(od.keys()), [t[0] for t in pairs])
    self.assertEqual(list(od.values()), [t[1] for t in pairs])
    self.assertEqual(list(od.items()), pairs)
    self.assertEqual(list(reversed(od)), [t[0] for t in reversed(pairs)])
    self.assertEqual(list(reversed(od.keys())), [t[0] for t in reversed(pairs)])
    self.assertEqual(list(reversed(od.values())), [t[1] for t in reversed(pairs)])
    self.assertEqual(list(reversed(od.items())), list(reversed(pairs)))
