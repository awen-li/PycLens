# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    with self.assertRaises(TypeError):
        OrderedDict().update([('a', 1), ('b', 2)], None)
    pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    od = OrderedDict()
    od.update(dict(pairs))
    self.assertEqual(sorted(od.items()), pairs)
    od = OrderedDict()
    od.update(**dict(pairs))
    self.assertEqual(sorted(od.items()), pairs)
    od = OrderedDict()
    od.update(pairs)
    self.assertEqual(list(od.items()), pairs)
    od = OrderedDict()
    od.update([('a', 1), ('b', 2), ('c', 9), ('d', 4)], c=3, e=5)
    self.assertEqual(list(od.items()), pairs)
    od = OrderedDict()
    od.update(self=23)
    self.assertEqual(list(od.items()), [('self', 23)])
    od = OrderedDict()
    od.update(other={})
    self.assertEqual(list(od.items()), [('other', {})])
    od = OrderedDict()
    od.update(red=5, blue=6, other=7, self=8)
    self.assertEqual(sorted(list(od.items())), [('blue', 6), ('other', 7), ('red', 5), ('self', 8)])
    d = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 44), ('e', 55)])
    d.update([('e', 5), ('f', 6)], g=7, d=4)
    self.assertEqual(list(d.items()), [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7)])
    self.assertRaises(TypeError, OrderedDict().update, 42)
    self.assertRaises(TypeError, OrderedDict().update, (), ())
    self.assertRaises(TypeError, OrderedDict.update)
    self.assertRaises(TypeError, OrderedDict().update, 42)
    self.assertRaises(TypeError, OrderedDict().update, (), ())
    self.assertRaises(TypeError, OrderedDict.update)
