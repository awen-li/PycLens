# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_package_compiled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_dir() as script_dir:
        pkg_dir = os.path.join(script_dir, 'test_pkg')
        make_pkg(pkg_dir)
        script_name = _make_test_script(pkg_dir, '__main__')
        compiled_name = py_compile.compile(script_name, doraise=True)
        os.remove(script_name)
        pyc_file = import_helper.make_legacy_pyc(script_name)
        self._check_script(['-m', 'test_pkg'], pyc_file, pyc_file, script_dir, 'test_pkg', importlib.machinery.SourcelessFileLoader, cwd=script_dir)
