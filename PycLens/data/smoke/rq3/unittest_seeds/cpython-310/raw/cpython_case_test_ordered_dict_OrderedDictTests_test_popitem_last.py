# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_popitem_last

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [(i, i) for i in range(30)]
    obj = OrderedDict(pairs)
    for i in range(8):
        obj.popitem(True)
    obj.popitem(True)
    obj.popitem(last=True)
    self.assertEqual(len(obj), 20)
