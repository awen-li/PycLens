# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_keyed_cascading_deletes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = weakref.WeakKeyDictionary()
    mutate = False

    class C(object):

        def __init__(self, i):
            self.value = i

        def __hash__(self):
            return hash(self.value)

        def __eq__(self, other):
            if mutate:
                del objs[-1]
            return self.value == other.value
    objs = [C(i) for i in range(4)]
    for o in objs:
        d[o] = o.value
    del o
    objs = list(d.keys())
    objs.reverse()
    mutate = True
    count = 0
    for o in objs:
        count += 1
        del d[o]
    gc_collect()
    self.assertEqual(len(d), 0)
    self.assertEqual(count, 2)
