# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_repr_recursive_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict()
    od[42] = od.values()
    r = repr(od)
    self.assertIsInstance(r, str)
    od[42] = od.items()
    r = repr(od)
    self.assertIsInstance(r, str)
