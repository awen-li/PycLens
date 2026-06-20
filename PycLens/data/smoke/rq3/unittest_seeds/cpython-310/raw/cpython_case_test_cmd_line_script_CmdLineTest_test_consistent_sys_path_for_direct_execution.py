# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_consistent_sys_path_for_direct_execution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = textwrap.dedent('            import sys\n            for entry in sys.path:\n                print(entry)\n            ')
    self.maxDiff = None
    with os_helper.temp_dir() as work_dir, os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, '__main__', script)
        p = spawn_python('-Es', script_name, cwd=work_dir)
        out_by_name = kill_python(p).decode().splitlines()
        self.assertEqual(out_by_name[0], script_dir)
        self.assertNotIn(work_dir, out_by_name)
        p = spawn_python('-Es', script_dir, cwd=work_dir)
        out_by_dir = kill_python(p).decode().splitlines()
        self.assertEqual(out_by_dir, out_by_name)
        p = spawn_python('-I', script_dir, cwd=work_dir)
        out_by_dir_isolated = kill_python(p).decode().splitlines()
        self.assertEqual(out_by_dir_isolated, out_by_dir, out_by_name)
