# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_construct_singletons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for const in (None, Ellipsis, NotImplemented):
        tp = type(const)
        self.assertIs(tp(), const)
        self.assertRaises(TypeError, tp, 1, 2)
        self.assertRaises(TypeError, tp, a=1, b=2)
