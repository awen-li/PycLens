# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_condition_with_binop_with_bools

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        if True or False:
            return 1
        return 0
    self.assertEqual(f(), 1)
    self.check_lnotab(f)
