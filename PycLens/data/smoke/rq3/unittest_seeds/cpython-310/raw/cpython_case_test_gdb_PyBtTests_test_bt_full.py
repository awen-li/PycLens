# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyBtTests_test_bt_full

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bt = self.get_stack_trace(script=self.get_sample_script(), cmds_after_breakpoint=['py-bt-full'])
    self.assertMultilineMatches(bt, '^.*\n#[0-9]+ Frame 0x-?[0-9a-f]+, for file .*gdb_sample.py, line 7, in bar \\(a=1, b=2, c=3\\)\n    baz\\(a, b, c\\)\n#[0-9]+ Frame 0x-?[0-9a-f]+, for file .*gdb_sample.py, line 4, in foo \\(a=1, b=2, c=3\\)\n    bar\\(a, b, c\\)\n#[0-9]+ Frame 0x-?[0-9a-f]+, for file .*gdb_sample.py, line 12, in <module> \\(\\)\n    foo\\(1, 2, 3\\)\n')
