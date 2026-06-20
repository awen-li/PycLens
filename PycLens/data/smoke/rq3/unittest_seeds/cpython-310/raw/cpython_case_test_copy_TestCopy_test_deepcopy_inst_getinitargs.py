# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_inst_getinitargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __init__(self, foo):
            self.foo = foo

        def __getinitargs__(self):
            return (self.foo,)

        def __eq__(self, other):
            return self.foo == other.foo
    x = C([42])
    y = copy.deepcopy(x)
    self.assertEqual(y, x)
    self.assertIsNot(y, x)
    self.assertIsNot(y.foo, x.foo)
