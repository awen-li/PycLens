# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    shuffle(pairs)
    od = OrderedDict(pairs)
    shuffle(pairs)
    while pairs:
        (k, v) = pairs.pop()
        self.assertEqual(od.pop(k), v)
    with self.assertRaises(KeyError):
        od.pop('xyz')
    self.assertEqual(len(od), 0)
    self.assertEqual(od.pop(k, 12345), 12345)

    class Missing(OrderedDict):

        def __missing__(self, key):
            return 0
    m = Missing(a=1)
    self.assertEqual(m.pop('b', 5), 5)
    self.assertEqual(m.pop('a', 6), 1)
    self.assertEqual(m.pop('a', 6), 6)
    self.assertEqual(m.pop('a', default=6), 6)
    with self.assertRaises(KeyError):
        m.pop('a')
