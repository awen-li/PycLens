# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyLocalsTests_test_locals_after_up

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bt = self.get_stack_trace(script=self.get_sample_script(), cmds_after_breakpoint=['py-up', 'py-up', 'py-locals'])
    self.assertMultilineMatches(bt, '.*\\na = 1\\nb = 2\\nc = 3\\n.*')
