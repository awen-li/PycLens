# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_deepcopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Tracer:

        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return self.value

        def __deepcopy__(self, memo=None):
            return Tracer(self.value + 1)
    t = Tracer(10)
    s = self.thetype([t])
    dup = copy.deepcopy(s)
    self.assertNotEqual(id(s), id(dup))
    for elem in dup:
        newt = elem
    self.assertNotEqual(id(t), id(newt))
    self.assertEqual(t.value + 1, newt.value)
