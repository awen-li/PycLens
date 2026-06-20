# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestBreakpoint_test_breakpoint_with_breakpointhook_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    my_breakpointhook = MagicMock()
    sys.breakpointhook = my_breakpointhook
    breakpoint()
    my_breakpointhook.assert_called_once_with()
