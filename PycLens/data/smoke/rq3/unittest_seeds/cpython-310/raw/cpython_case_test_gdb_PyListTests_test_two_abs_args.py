# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyListTests_test_two_abs_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bt = self.get_stack_trace(script=self.get_sample_script(), cmds_after_breakpoint=['py-list 1,3'])
    self.assertListing('   1    # Sample script for use by test_gdb.py\n   2    \n   3    def foo(a, b, c):\n', bt)
