# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_reconstruct_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __reduce__(self):
            return (C, (), self.__dict__)

        def __eq__(self, other):
            return self.__dict__ == other.__dict__
    x = C()
    x.foo = [42]
    y = copy.copy(x)
    self.assertEqual(y, x)
    y = copy.deepcopy(x)
    self.assertEqual(y, x)
    self.assertIsNot(y.foo, x.foo)
