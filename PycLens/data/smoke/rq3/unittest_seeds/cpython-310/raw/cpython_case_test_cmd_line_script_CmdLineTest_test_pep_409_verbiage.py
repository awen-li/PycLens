# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_pep_409_verbiage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = textwrap.dedent('            try:\n                raise ValueError\n            except:\n                raise NameError from None\n            ')
    with os_helper.temp_dir() as script_dir:
        script_name = _make_test_script(script_dir, 'script', script)
        (exitcode, stdout, stderr) = assert_python_failure(script_name)
        text = stderr.decode('ascii').split('\n')
        self.assertEqual(len(text), 5)
        self.assertTrue(text[0].startswith('Traceback'))
        self.assertTrue(text[1].startswith('  File '))
        self.assertTrue(text[3].startswith('NameError'))
