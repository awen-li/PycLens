# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyListTests_test_basic_command

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bt = self.get_stack_trace(script=self.get_sample_script(), cmds_after_breakpoint=['py-list'])
    self.assertListing('   5    \n   6    def bar(a, b, c):\n   7        baz(a, b, c)\n   8    \n   9    def baz(*args):\n >10        id(42)\n  11    \n  12    foo(1, 2, 3)\n', bt)
