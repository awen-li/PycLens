# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeop.py
# case: CodeopTests_test_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings(('.*literal', SyntaxWarning), ('.*invalid', DeprecationWarning)) as w:
        compile_command("'\\e' is 0")
        self.assertEqual(len(w.warnings), 2)
    with warnings.catch_warnings(), self.assertRaises(SyntaxError):
        warnings.simplefilter('error', SyntaxWarning)
        compile_command('1 is 1', symbol='exec')
    with warnings.catch_warnings(), self.assertRaises(SyntaxError):
        warnings.simplefilter('error', DeprecationWarning)
        compile_command("'\\e'", symbol='exec')
