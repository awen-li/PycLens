# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: CPythonOrderedDictTests_test_key_change_during_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict.fromkeys('abcde')
    self.assertEqual(list(od), list('abcde'))
    with self.assertRaises(RuntimeError):
        for (i, k) in enumerate(od):
            od.move_to_end(k)
            self.assertLess(i, 5)
    with self.assertRaises(RuntimeError):
        for k in od:
            od['f'] = None
    with self.assertRaises(RuntimeError):
        for k in od:
            del od['c']
    self.assertEqual(list(od), list('bdeaf'))
