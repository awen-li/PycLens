# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_reduce_4tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(list):

        def __reduce__(self):
            return (C, (), self.__dict__, iter(self))

        def __eq__(self, other):
            return list(self) == list(other) and self.__dict__ == other.__dict__
    x = C([[1, 2], 3])
    y = copy.copy(x)
    self.assertEqual(x, y)
    self.assertIsNot(x, y)
    self.assertIs(x[0], y[0])
    y = copy.deepcopy(x)
    self.assertEqual(x, y)
    self.assertIsNot(x, y)
    self.assertIsNot(x[0], y[0])
