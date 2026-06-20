# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_reduce_not_too_fat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    od = OrderedDict(pairs)
    self.assertIsInstance(od.__dict__, dict)
    self.assertIsNone(od.__reduce__()[2])
    od.x = 10
    self.assertEqual(od.__dict__['x'], 10)
    self.assertEqual(od.__reduce__()[2], {'x': 10})
