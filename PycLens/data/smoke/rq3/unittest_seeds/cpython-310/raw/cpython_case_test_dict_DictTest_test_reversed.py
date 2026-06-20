# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_reversed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'a': 1, 'b': 2, 'foo': 0, 'c': 3, 'd': 4}
    del d['foo']
    r = reversed(d)
    self.assertEqual(list(r), list('dcba'))
    self.assertRaises(StopIteration, next, r)
