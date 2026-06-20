# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_move_to_end

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict.fromkeys('abcde')
    self.assertEqual(list(od), list('abcde'))
    od.move_to_end('c')
    self.assertEqual(list(od), list('abdec'))
    od.move_to_end('c', False)
    self.assertEqual(list(od), list('cabde'))
    od.move_to_end('c', False)
    self.assertEqual(list(od), list('cabde'))
    od.move_to_end('e')
    self.assertEqual(list(od), list('cabde'))
    od.move_to_end('b', last=False)
    self.assertEqual(list(od), list('bcade'))
    with self.assertRaises(KeyError):
        od.move_to_end('x')
    with self.assertRaises(KeyError):
        od.move_to_end('x', False)
