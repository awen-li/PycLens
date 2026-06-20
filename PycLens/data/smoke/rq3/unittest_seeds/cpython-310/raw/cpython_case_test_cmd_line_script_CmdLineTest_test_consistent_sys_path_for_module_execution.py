# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_consistent_sys_path_for_module_execution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = textwrap.dedent('            import sys\n            for entry in sys.path:\n                print(entry)\n            ')
    self.maxDiff = None
    with os_helper.temp_dir() as work_dir:
        script_dir = os.path.join(work_dir, 'script_pkg')
        os.mkdir(script_dir)
        script_name = _make_test_script(script_dir, '__main__', script)
        p = spawn_python('-sm', 'script_pkg.__main__', cwd=work_dir)
        out_by_module = kill_python(p).decode().splitlines()
        self.assertEqual(out_by_module[0], work_dir)
        self.assertNotIn(script_dir, out_by_module)
        p = spawn_python('-sm', 'script_pkg', cwd=work_dir)
        out_by_package = kill_python(p).decode().splitlines()
        self.assertEqual(out_by_package, out_by_module)
        (exitcode, stdout, stderr) = assert_python_failure('-Im', 'script_pkg', cwd=work_dir)
        traceback_lines = stderr.decode().splitlines()
        self.assertIn('No module named script_pkg', traceback_lines[-1])
