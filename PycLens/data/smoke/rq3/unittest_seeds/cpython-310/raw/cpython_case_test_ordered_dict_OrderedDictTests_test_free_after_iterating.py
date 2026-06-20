# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_free_after_iterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.check_free_after_iterating(self, iter, self.OrderedDict)
    support.check_free_after_iterating(self, lambda d: iter(d.keys()), self.OrderedDict)
    support.check_free_after_iterating(self, lambda d: iter(d.values()), self.OrderedDict)
    support.check_free_after_iterating(self, lambda d: iter(d.items()), self.OrderedDict)
