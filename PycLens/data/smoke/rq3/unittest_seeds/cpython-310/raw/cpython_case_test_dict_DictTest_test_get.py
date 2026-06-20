# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    self.assertIs(d.get('c'), None)
    self.assertEqual(d.get('c', 3), 3)
    d = {'a': 1, 'b': 2}
    self.assertIs(d.get('c'), None)
    self.assertEqual(d.get('c', 3), 3)
    self.assertEqual(d.get('a'), 1)
    self.assertEqual(d.get('a', 3), 1)
    self.assertRaises(TypeError, d.get)
    self.assertRaises(TypeError, d.get, None, None, None)
