# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_merge_code_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f1 = lambda x: x.y.z
    f2 = lambda a: a.b.c
    self.assertIs(f1.__code__.co_linetable, f2.__code__.co_linetable)
    self.assertIs(f1.__code__.co_code, f2.__code__.co_code)
