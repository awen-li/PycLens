# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, sys.exit, 42, 42)
    with self.assertRaises(SystemExit) as cm:
        sys.exit()
    self.assertIsNone(cm.exception.code)
    (rc, out, err) = assert_python_ok('-c', 'import sys; sys.exit()')
    self.assertEqual(rc, 0)
    self.assertEqual(out, b'')
    self.assertEqual(err, b'')
    with self.assertRaises(SystemExit) as cm:
        sys.exit(42)
    self.assertEqual(cm.exception.code, 42)
    with self.assertRaises(SystemExit) as cm:
        sys.exit((42,))
    self.assertEqual(cm.exception.code, 42)
    with self.assertRaises(SystemExit) as cm:
        sys.exit('exit')
    self.assertEqual(cm.exception.code, 'exit')
    with self.assertRaises(SystemExit) as cm:
        sys.exit((17, 23))
    self.assertEqual(cm.exception.code, (17, 23))
    (rc, out, err) = assert_python_failure('-c', 'raise SystemExit(47)')
    self.assertEqual(rc, 47)
    self.assertEqual(out, b'')
    self.assertEqual(err, b'')

    def check_exit_message(code, expected, **env_vars):
        (rc, out, err) = assert_python_failure('-c', code, **env_vars)
        self.assertEqual(rc, 1)
        self.assertEqual(out, b'')
        self.assertTrue(err.startswith(expected), "%s doesn't start with %s" % (ascii(err), ascii(expected)))
    check_exit_message('import sys; sys.stderr.write("unflushed,"); sys.exit("message")', b'unflushed,message')
    check_exit_message('import sys; sys.exit("surrogates:\\uDCFF")', b'surrogates:\\udcff')
    check_exit_message('import sys; sys.exit("h\\xe9")', b'h\xe9', PYTHONIOENCODING='latin-1')
