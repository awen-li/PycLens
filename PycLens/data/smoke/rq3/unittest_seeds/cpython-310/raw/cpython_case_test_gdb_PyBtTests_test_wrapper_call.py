# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyBtTests_test_wrapper_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmd = textwrap.dedent('\n            class MyList(list):\n                def __init__(self):\n                    super().__init__()   # wrapper_call()\n\n            id("first break point")\n            l = MyList()\n        ')
    cmds_after_breakpoint = ['break wrapper_call', 'continue']
    if CET_PROTECTION:
        cmds_after_breakpoint.append('next')
    cmds_after_breakpoint.append('py-bt')
    gdb_output = self.get_stack_trace(cmd, cmds_after_breakpoint=cmds_after_breakpoint)
    self.assertRegex(gdb_output, "<method-wrapper u?'__init__' of MyList object at ")
