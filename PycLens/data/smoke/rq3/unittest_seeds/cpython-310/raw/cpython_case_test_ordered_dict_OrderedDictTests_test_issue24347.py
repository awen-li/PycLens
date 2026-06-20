# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_issue24347

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict

    class Key:

        def __hash__(self):
            return randrange(100000)
    od = OrderedDict()
    for i in range(100):
        key = Key()
        od[key] = i
    with self.assertRaises(KeyError):
        list(od.values())
    with self.assertRaises(KeyError):
        list(od.items())
    with self.assertRaises(KeyError):
        repr(od)
    with self.assertRaises(KeyError):
        od.copy()
