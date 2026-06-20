# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_setdefault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    shuffle(pairs)
    od = OrderedDict(pairs)
    pair_order = list(od.items())
    self.assertEqual(od.setdefault('a', 10), 3)
    self.assertEqual(list(od.items()), pair_order)
    self.assertEqual(od.setdefault('x', 10), 10)
    self.assertEqual(list(od.items())[-1], ('x', 10))
    self.assertEqual(od.setdefault('g', default=9), 9)

    class Missing(OrderedDict):

        def __missing__(self, key):
            return 0
    self.assertEqual(Missing().setdefault(5, 9), 9)
