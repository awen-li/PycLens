# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_issue8202

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        with os_helper.change_cwd(path=script_dir):
            pkg_dir = os.path.join(script_dir, 'test_pkg')
            make_pkg(pkg_dir, "import sys; print('init_argv0==%r' % sys.argv[0])")
            script_name = _make_test_script(pkg_dir, 'script')
            (rc, out, err) = assert_python_ok('-m', 'test_pkg.script', *example_args, __isolated=False)
            if verbose > 1:
                print(repr(out))
            expected = 'init_argv0==%r' % '-m'
            self.assertIn(expected.encode('utf-8'), out)
            self._check_output(script_name, rc, out, script_name, script_name, script_dir, 'test_pkg', importlib.machinery.SourceFileLoader)
