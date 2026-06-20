# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_valued_iters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (dict, objects) = self.make_weak_valued_dict()
    self.check_iters(dict)
    refs = dict.valuerefs()
    self.assertEqual(len(refs), len(objects))
    objects2 = list(objects)
    for wr in refs:
        ob = wr()
        self.assertEqual(ob, dict[ob.arg])
        self.assertEqual(ob.arg, dict[ob.arg].arg)
        objects2.remove(ob)
    self.assertEqual(len(objects2), 0)
    objects2 = list(objects)
    self.assertEqual(len(list(dict.itervaluerefs())), len(objects))
    for wr in dict.itervaluerefs():
        ob = wr()
        self.assertEqual(ob, dict[ob.arg])
        self.assertEqual(ob.arg, dict[ob.arg].arg)
        objects2.remove(ob)
    self.assertEqual(len(objects2), 0)
