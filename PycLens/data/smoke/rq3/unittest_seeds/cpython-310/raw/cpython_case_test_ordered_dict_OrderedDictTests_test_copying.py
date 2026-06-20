# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_copying

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    od = OrderedDict(pairs)

    def check(dup):
        msg = '\ncopy: %s\nod: %s' % (dup, od)
        self.assertIsNot(dup, od, msg)
        self.assertEqual(dup, od)
        self.assertEqual(list(dup.items()), list(od.items()))
        self.assertEqual(len(dup), len(od))
        self.assertEqual(type(dup), type(od))
    check(od.copy())
    check(copy.copy(od))
    check(copy.deepcopy(od))
    with replaced_module('collections', self.module):
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.subTest(proto=proto):
                check(pickle.loads(pickle.dumps(od, proto)))
    check(eval(repr(od)))
    update_test = OrderedDict()
    update_test.update(od)
    check(update_test)
    check(OrderedDict(od))
