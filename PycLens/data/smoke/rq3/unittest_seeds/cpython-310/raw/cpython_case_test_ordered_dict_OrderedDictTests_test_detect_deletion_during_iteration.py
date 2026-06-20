# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_detect_deletion_during_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict.fromkeys('abc')
    it = iter(od)
    key = next(it)
    del od[key]
    with self.assertRaises(Exception):
        next(it)
