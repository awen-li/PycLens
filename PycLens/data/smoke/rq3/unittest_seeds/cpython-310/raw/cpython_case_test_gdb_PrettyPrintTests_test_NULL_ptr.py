# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_NULL_ptr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (gdb_repr, gdb_output) = self.get_gdb_repr('id(42)', cmds_after_breakpoint=['set variable v=0', 'backtrace'])
    self.assertEqual(gdb_repr, '0x0')
