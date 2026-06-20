# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_list_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(list):
        pass
    x = C([[1, 2], 3])
    x.foo = [4, 5]
    y = copy.copy(x)
    self.assertEqual(list(x), list(y))
    self.assertEqual(x.foo, y.foo)
    self.assertIs(x[0], y[0])
    self.assertIs(x.foo, y.foo)
