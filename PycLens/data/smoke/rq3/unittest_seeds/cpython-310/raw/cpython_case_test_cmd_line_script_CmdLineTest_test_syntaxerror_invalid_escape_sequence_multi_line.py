# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_syntaxerror_invalid_escape_sequence_multi_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = 'foo = """\\q"""\n'
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, 'script', script)
        (exitcode, stdout, stderr) = assert_python_failure('-Werror', script_name)
        self.assertEqual(stderr.splitlines()[-3:], [b'    foo = """\\q"""', b'          ^^^^^^^^', b"SyntaxError: invalid escape sequence '\\q'"])
