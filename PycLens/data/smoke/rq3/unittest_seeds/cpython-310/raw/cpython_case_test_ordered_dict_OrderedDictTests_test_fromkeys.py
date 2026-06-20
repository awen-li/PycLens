# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_fromkeys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict.fromkeys('abc')
    self.assertEqual(list(od.items()), [(c, None) for c in 'abc'])
    od = OrderedDict.fromkeys('abc', value=None)
    self.assertEqual(list(od.items()), [(c, None) for c in 'abc'])
    od = OrderedDict.fromkeys('abc', value=0)
    self.assertEqual(list(od.items()), [(c, 0) for c in 'abc'])
