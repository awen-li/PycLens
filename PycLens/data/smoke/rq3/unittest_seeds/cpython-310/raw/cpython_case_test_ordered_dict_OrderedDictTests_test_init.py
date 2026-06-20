# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    with self.assertRaises(TypeError):
        OrderedDict([('a', 1), ('b', 2)], None)
    pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    self.assertEqual(sorted(OrderedDict(dict(pairs)).items()), pairs)
    self.assertEqual(sorted(OrderedDict(**dict(pairs)).items()), pairs)
    self.assertEqual(list(OrderedDict(pairs).items()), pairs)
    self.assertEqual(list(OrderedDict([('a', 1), ('b', 2), ('c', 9), ('d', 4)], c=3, e=5).items()), pairs)
    self.assertEqual(list(OrderedDict(self=42).items()), [('self', 42)])
    self.assertEqual(list(OrderedDict(other=42).items()), [('other', 42)])
    self.assertRaises(TypeError, OrderedDict, 42)
    self.assertRaises(TypeError, OrderedDict, (), ())
    self.assertRaises(TypeError, OrderedDict.__init__)
    d = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 44), ('e', 55)])
    d.__init__([('e', 5), ('f', 6)], g=7, d=4)
    self.assertEqual(list(d.items()), [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7)])
