# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_pickle_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict()
    od[1] = od
    with replaced_module('collections', self.module):
        for proto in range(-1, pickle.HIGHEST_PROTOCOL + 1):
            dup = pickle.loads(pickle.dumps(od, proto))
            self.assertIsNot(dup, od)
            self.assertEqual(list(dup.keys()), [1])
            self.assertIs(dup[1], dup)
