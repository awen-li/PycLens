# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_sorted_iterators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    with self.assertRaises(TypeError):
        OrderedDict([('a', 1), ('b', 2)], None)
    pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    od = OrderedDict(pairs)
    self.assertEqual(sorted(od), [t[0] for t in pairs])
    self.assertEqual(sorted(od.keys()), [t[0] for t in pairs])
    self.assertEqual(sorted(od.values()), [t[1] for t in pairs])
    self.assertEqual(sorted(od.items()), pairs)
    self.assertEqual(sorted(reversed(od)), sorted([t[0] for t in reversed(pairs)]))
