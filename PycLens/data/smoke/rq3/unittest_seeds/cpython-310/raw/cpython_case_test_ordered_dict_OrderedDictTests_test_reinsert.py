# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_reinsert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    del od['a']
    self.assertEqual(list(od.items()), [('b', 2)])
    od['a'] = 1
    self.assertEqual(list(od.items()), [('b', 2), ('a', 1)])
