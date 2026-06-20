# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMiscTest_test_failed_import_during_compiling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys;sys.modules[\'unicodedata\'] = None;eval("\'\\\\N{SOFT HYPHEN}\'")'
    result = script_helper.assert_python_failure('-c', code)
    error = "SyntaxError: (unicode error) \\N escapes not supported (can't load unicodedata module)"
    self.assertIn(error, result.err.decode('ascii'))
