# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_reduce_6tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def state_setter(*args, **kwargs):
        self.fail("shouldn't call this")

    class C:

        def __reduce__(self):
            return (C, (), self.__dict__, None, None, state_setter)
    x = C()
    with self.assertRaises(TypeError):
        copy.copy(x)
    with self.assertRaises(TypeError):
        copy.deepcopy(x)
