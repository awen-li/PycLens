# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_script_as_dev_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = 'print("12345678912345678912345")'
    with os_helper.temp_dir() as work_dir:
        script_name = _make_test_script(work_dir, 'script.py', script)
        with open(script_name, 'r') as fp:
            p = spawn_python(f'/dev/fd/{fp.fileno()}', close_fds=False, pass_fds=(0, 1, 2, fp.fileno()))
            (out, err) = p.communicate()
            self.assertEqual(out, b'12345678912345678912345\n')
