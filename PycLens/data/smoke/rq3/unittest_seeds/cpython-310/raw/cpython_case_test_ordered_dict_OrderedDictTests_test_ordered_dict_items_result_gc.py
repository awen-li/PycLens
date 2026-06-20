# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_ordered_dict_items_result_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = iter(self.OrderedDict({None: []}).items())
    gc.collect()
    self.assertTrue(gc.is_tracked(next(it)))
