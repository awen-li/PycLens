# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_frames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gdb_output = self.get_stack_trace('\ndef foo(a, b, c):\n    pass\n\nfoo(3, 4, 5)\nid(foo.__code__)', breakpoint='builtin_id', cmds_after_breakpoint=['print (PyFrameObject*)(((PyCodeObject*)v)->co_zombieframe)'])
    self.assertTrue(re.match('.*\\s+\\$1 =\\s+Frame 0x-?[0-9a-f]+, for file <string>, line 3, in foo \\(\\)\\s+.*', gdb_output, re.DOTALL), 'Unexpected gdb representation: %r\n%s' % (gdb_output, gdb_output))
