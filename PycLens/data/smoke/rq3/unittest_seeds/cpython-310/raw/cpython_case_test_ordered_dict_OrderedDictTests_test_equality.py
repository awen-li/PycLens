# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    shuffle(pairs)
    od1 = OrderedDict(pairs)
    od2 = OrderedDict(pairs)
    self.assertEqual(od1, od2)
    pairs = pairs[2:] + pairs[:2]
    od2 = OrderedDict(pairs)
    self.assertNotEqual(od1, od2)
    self.assertEqual(od1, dict(od2))
    self.assertEqual(dict(od2), od1)
    self.assertNotEqual(od1, OrderedDict(pairs[:-1]))
