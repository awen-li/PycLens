# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_reflexive_inst

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass
    x = C()
    x.foo = x
    y = copy.deepcopy(x)
    self.assertIsNot(y, x)
    self.assertIs(y.foo, y)
