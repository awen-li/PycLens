# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyBtTests_test_bt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bt = self.get_stack_trace(script=self.get_sample_script(), cmds_after_breakpoint=['py-bt'])
    self.assertMultilineMatches(bt, '^.*\nTraceback \\(most recent call first\\):\n  <built-in method id of module object .*>\n  File ".*gdb_sample.py", line 10, in baz\n    id\\(42\\)\n  File ".*gdb_sample.py", line 7, in bar\n    baz\\(a, b, c\\)\n  File ".*gdb_sample.py", line 4, in foo\n    bar\\(a, b, c\\)\n  File ".*gdb_sample.py", line 12, in <module>\n    foo\\(1, 2, 3\\)\n')
