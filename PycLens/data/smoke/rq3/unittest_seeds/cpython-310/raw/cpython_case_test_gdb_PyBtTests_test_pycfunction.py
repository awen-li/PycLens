# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PyBtTests_test_pycfunction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (func_name, args, expected_frame) in (('meth_varargs', '', 1), ('meth_varargs_keywords', '', 1), ('meth_o', '[]', 1), ('meth_noargs', '', 1), ('meth_fastcall', '', 1), ('meth_fastcall_keywords', '', 1)):
        for obj in ('_testcapi', '_testcapi.MethClass', '_testcapi.MethClass()', '_testcapi.MethStatic()'):
            with self.subTest(f'{obj}.{func_name}'):
                cmd = textwrap.dedent(f'\n                        import _testcapi\n                        def foo():\n                            {obj}.{func_name}({args})\n                        def bar():\n                            foo()\n                        bar()\n                    ')
                gdb_output = self.get_stack_trace(cmd, breakpoint=func_name, cmds_after_breakpoint=['bt', 'py-bt'], ignore_stderr=True)
                self.assertIn(f'<built-in method {func_name}', gdb_output)
                gdb_output = self.get_stack_trace(cmd, breakpoint=func_name, cmds_after_breakpoint=['py-bt-full'], ignore_stderr=True)
                self.assertIn(f'#{expected_frame} <built-in method {func_name}', gdb_output)
