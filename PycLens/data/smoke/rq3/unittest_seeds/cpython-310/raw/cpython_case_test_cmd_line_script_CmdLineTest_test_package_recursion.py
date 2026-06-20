# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_package_recursion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        pkg_dir = os.path.join(script_dir, 'test_pkg')
        make_pkg(pkg_dir)
        main_dir = os.path.join(pkg_dir, '__main__')
        make_pkg(main_dir)
        msg = "Cannot use package as __main__ module; 'test_pkg' is a package and cannot be directly executed"
        self._check_import_error(['-m', 'test_pkg'], msg, cwd=script_dir)
