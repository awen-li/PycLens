# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_issue8202_dash_c_file_ignored

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        with os_helper.change_cwd(path=script_dir):
            with open('-c', 'w', encoding='utf-8') as f:
                f.write('data')
                (rc, out, err) = assert_python_ok('-c', 'import sys; print("sys.path[0]==%r" % sys.path[0])', __isolated=False)
                if verbose > 1:
                    print(repr(out))
                expected = 'sys.path[0]==%r' % ''
                self.assertIn(expected.encode('utf-8'), out)
