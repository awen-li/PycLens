# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (dict, objects) = self.make_weak_keyed_dict()
    for o in objects:
        self.assertEqual(weakref.getweakrefcount(o), 1, 'wrong number of weak references to %r!' % o)
        self.assertIs(o.arg, dict[o], 'wrong object returned by weak dict!')
    items1 = dict.items()
    items2 = dict.copy().items()
    self.assertEqual(set(items1), set(items2), 'cloning of weak-keyed dictionary did not work!')
    del items1, items2
    self.assertEqual(len(dict), self.COUNT)
    del objects[0]
    gc_collect()
    self.assertEqual(len(dict), self.COUNT - 1, 'deleting object did not cause dictionary update')
    del objects, o
    gc_collect()
    self.assertEqual(len(dict), 0, 'deleting the keys did not clear the dictionary')
    o = Object(42)
    dict[o] = 'What is the meaning of the universe?'
    self.assertIn(o, dict)
    self.assertNotIn(34, dict)
