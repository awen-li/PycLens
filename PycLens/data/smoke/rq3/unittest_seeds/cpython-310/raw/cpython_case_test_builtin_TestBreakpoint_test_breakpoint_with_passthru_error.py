# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestBreakpoint_test_breakpoint_with_passthru_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def my_breakpointhook():
        pass
    sys.breakpointhook = my_breakpointhook
    self.assertRaises(TypeError, breakpoint, 1, 2, 3, four=4, five=5)
