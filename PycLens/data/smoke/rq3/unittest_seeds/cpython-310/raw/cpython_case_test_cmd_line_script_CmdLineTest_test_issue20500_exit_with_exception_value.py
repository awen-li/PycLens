# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_issue20500_exit_with_exception_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = textwrap.dedent("            import sys\n            error = None\n            try:\n                raise ValueError('some text')\n            except ValueError as err:\n                error = err\n\n            if error:\n                sys.exit(error)\n            ")
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, 'script', script)
        (exitcode, stdout, stderr) = assert_python_failure(script_name)
        text = stderr.decode('ascii')
        self.assertEqual(text.rstrip(), 'some text')
