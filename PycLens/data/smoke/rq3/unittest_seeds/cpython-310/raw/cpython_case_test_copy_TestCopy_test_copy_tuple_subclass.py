# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_tuple_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(tuple):
        pass
    x = C([1, 2, 3])
    self.assertEqual(tuple(x), (1, 2, 3))
    y = copy.copy(x)
    self.assertEqual(tuple(y), (1, 2, 3))
