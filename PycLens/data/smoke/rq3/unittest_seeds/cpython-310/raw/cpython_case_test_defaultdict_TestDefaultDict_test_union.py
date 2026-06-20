# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = defaultdict(int, {1: 1, 2: 2})
    s = defaultdict(str, {0: 'zero', 1: 'one'})
    i_s = i | s
    self.assertIs(i_s.default_factory, int)
    self.assertDictEqual(i_s, {1: 'one', 2: 2, 0: 'zero'})
    self.assertEqual(list(i_s), [1, 2, 0])
    s_i = s | i
    self.assertIs(s_i.default_factory, str)
    self.assertDictEqual(s_i, {0: 'zero', 1: 1, 2: 2})
    self.assertEqual(list(s_i), [0, 1, 2])
    i_ds = i | dict(s)
    self.assertIs(i_ds.default_factory, int)
    self.assertDictEqual(i_ds, {1: 'one', 2: 2, 0: 'zero'})
    self.assertEqual(list(i_ds), [1, 2, 0])
    ds_i = dict(s) | i
    self.assertIs(ds_i.default_factory, int)
    self.assertDictEqual(ds_i, {0: 'zero', 1: 1, 2: 2})
    self.assertEqual(list(ds_i), [0, 1, 2])
    with self.assertRaises(TypeError):
        i | list(s.items())
    with self.assertRaises(TypeError):
        list(s.items()) | i
    i |= list(s.items())
    self.assertIs(i.default_factory, int)
    self.assertDictEqual(i, {1: 'one', 2: 2, 0: 'zero'})
    self.assertEqual(list(i), [1, 2, 0])
    with self.assertRaises(TypeError):
        i |= None
