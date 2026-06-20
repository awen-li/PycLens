# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_issue20884

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        script_name = os.path.join(script_dir, 'issue20884.py')
        with open(script_name, 'w', encoding='latin1', newline='\n') as f:
            f.write('#coding: iso-8859-1\n')
            f.write('"""\n')
            for _ in range(30):
                f.write('x' * 80 + '\n')
            f.write('"""\n')
        with os_helper.change_cwd(path=script_dir):
            (rc, out, err) = assert_python_ok(script_name)
        self.assertEqual(b'', out)
        self.assertEqual(b'', err)
