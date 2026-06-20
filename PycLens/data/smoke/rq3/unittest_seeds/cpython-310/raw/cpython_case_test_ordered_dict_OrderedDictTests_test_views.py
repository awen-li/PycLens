# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_views

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    s = 'the quick brown fox jumped over a lazy dog yesterday before dawn'.split()
    od = OrderedDict.fromkeys(s)
    self.assertEqual(od.keys(), dict(od).keys())
    self.assertEqual(od.items(), dict(od).items())
