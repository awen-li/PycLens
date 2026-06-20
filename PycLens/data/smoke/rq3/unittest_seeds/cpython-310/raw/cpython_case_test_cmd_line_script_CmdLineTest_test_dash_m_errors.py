# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line_script.py
# case: CmdLineTest_test_dash_m_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = (('builtins', b'No code object available'), ('builtins.x', b'Error while finding module specification.*ModuleNotFoundError'), ('builtins.x.y', b'Error while finding module specification.*ModuleNotFoundError.*No module named.*not a package'), ('os.path', b'loader.*cannot handle'), ('importlib', b'No module named.*is a package and cannot be directly executed'), ('importlib.nonexistent', b'No module named'), ('.unittest', b'Relative module names not supported'))
    for (name, regex) in tests:
        with self.subTest(name):
            (rc, _, err) = assert_python_failure('-m', name)
            self.assertEqual(rc, 1)
            self.assertRegex(err, regex)
            self.assertNotIn(b'Traceback', err)
