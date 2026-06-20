# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_for_distinct_code_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        f1 = lambda x=1: x
        f2 = lambda x=2: x
        return (f1, f2)
    (f1, f2) = f()
    self.assertNotEqual(id(f1.__code__), id(f2.__code__))
