# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_list_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(list):
        pass
    x = C([[1, 2], 3])
    x.foo = [4, 5]
    y = copy.deepcopy(x)
    self.assertEqual(list(x), list(y))
    self.assertEqual(x.foo, y.foo)
    self.assertIsNot(x[0], y[0])
    self.assertIsNot(x.foo, y.foo)
