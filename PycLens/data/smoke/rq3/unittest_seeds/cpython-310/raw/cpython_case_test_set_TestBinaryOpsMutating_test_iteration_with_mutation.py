# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestBinaryOpsMutating_test_iteration_with_mutation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f1(a, b):
        for x in a:
            pass
        for y in b:
            pass

    def f2(a, b):
        for y in b:
            pass
        for x in a:
            pass

    def f3(a, b):
        for (x, y) in zip(a, b):
            pass
    self.check_set_op_does_not_crash(f1)
    self.check_set_op_does_not_crash(f2)
    self.check_set_op_does_not_crash(f3)
