# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyPrintTests_test_printing_builtin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bt = self.get_stack_trace(script=self.get_sample_script(), cmds_after_breakpoint=['py-up', 'py-print len'])
    self.assertMultilineMatches(bt, ".*\\nbuiltin 'len' = <built-in method len of module object at remote 0x-?[0-9a-f]+>\\n.*")
