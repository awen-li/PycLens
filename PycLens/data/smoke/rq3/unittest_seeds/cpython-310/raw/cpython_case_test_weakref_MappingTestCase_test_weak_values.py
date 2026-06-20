# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (dict, objects) = self.make_weak_valued_dict()
    for o in objects:
        self.assertEqual(weakref.getweakrefcount(o), 1)
        self.assertIs(o, dict[o.arg], 'wrong object returned by weak dict!')
    items1 = list(dict.items())
    items2 = list(dict.copy().items())
    items1.sort()
    items2.sort()
    self.assertEqual(items1, items2, 'cloning of weak-valued dictionary did not work!')
    del items1, items2
    self.assertEqual(len(dict), self.COUNT)
    del objects[0]
    gc_collect()
    self.assertEqual(len(dict), self.COUNT - 1, 'deleting object did not cause dictionary update')
    del objects, o
    gc_collect()
    self.assertEqual(len(dict), 0, 'deleting the values did not clear the dictionary')
    dict = weakref.WeakValueDictionary()
    self.assertRaises(KeyError, dict.__getitem__, 1)
    dict[2] = C()
    gc_collect()
    self.assertRaises(KeyError, dict.__getitem__, 2)
