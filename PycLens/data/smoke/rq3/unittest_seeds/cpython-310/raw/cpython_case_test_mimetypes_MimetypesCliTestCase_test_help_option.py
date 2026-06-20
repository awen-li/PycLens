# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: MimetypesCliTestCase_test_help_option

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.patch(self, sys, 'argv', [sys.executable, '-h'])
    with support.captured_stdout() as output:
        with self.assertRaises(SystemExit) as cm:
            mimetypes._main()
    self.assertIn('Usage: mimetypes.py', output.getvalue())
    self.assertEqual(cm.exception.code, 0)
