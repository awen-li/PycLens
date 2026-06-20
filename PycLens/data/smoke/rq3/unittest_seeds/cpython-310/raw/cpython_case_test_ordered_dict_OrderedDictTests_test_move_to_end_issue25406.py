# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_move_to_end_issue25406

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict.fromkeys('abc')
    od.move_to_end('c', last=False)
    self.assertEqual(list(od), list('cab'))
    od.move_to_end('a', last=False)
    self.assertEqual(list(od), list('acb'))
    od = OrderedDict.fromkeys('abc')
    od.move_to_end('a')
    self.assertEqual(list(od), list('bca'))
    od.move_to_end('c')
    self.assertEqual(list(od), list('bac'))
