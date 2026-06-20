# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_getting_backtrace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gdb_output = self.get_stack_trace('id(42)')
    self.assertTrue(BREAKPOINT_FN in gdb_output)
