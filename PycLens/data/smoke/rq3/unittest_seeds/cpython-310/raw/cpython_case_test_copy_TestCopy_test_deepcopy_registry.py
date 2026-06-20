# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_registry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __new__(cls, foo):
            obj = object.__new__(cls)
            obj.foo = foo
            return obj

    def pickle_C(obj):
        return (C, (obj.foo,))
    x = C(42)
    self.assertRaises(TypeError, copy.deepcopy, x)
    copyreg.pickle(C, pickle_C, C)
    y = copy.deepcopy(x)
    self.assertIsNot(x, y)
    self.assertEqual(type(y), C)
    self.assertEqual(y.foo, x.foo)
