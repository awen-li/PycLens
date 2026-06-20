# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_elim_jump_to_uncond_jump

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        if a:
            if c or d:
                foo()
        else:
            baz()
    self.check_jump_targets(f)
    self.check_lnotab(f)
