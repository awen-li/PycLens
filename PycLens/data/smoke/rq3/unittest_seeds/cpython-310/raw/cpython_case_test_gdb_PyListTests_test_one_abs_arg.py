# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyListTests_test_one_abs_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bt = self.get_stack_trace(script=self.get_sample_script(), cmds_after_breakpoint=['py-list 9'])
    self.assertListing('   9    def baz(*args):\n >10        id(42)\n  11    \n  12    foo(1, 2, 3)\n', bt)
