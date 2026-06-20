# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyBtTests_test_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmd = 'from gc import collect\nid(42)\ndef foo():\n    collect()\ndef bar():\n    foo()\nbar()\n'
    gdb_output = self.get_stack_trace(cmd, cmds_after_breakpoint=['break update_refs', 'continue', 'py-bt'])
    self.assertIn('Garbage-collecting', gdb_output)
    gdb_output = self.get_stack_trace(cmd, cmds_after_breakpoint=['break update_refs', 'continue', 'py-bt-full'])
    self.assertIn('Garbage-collecting', gdb_output)
