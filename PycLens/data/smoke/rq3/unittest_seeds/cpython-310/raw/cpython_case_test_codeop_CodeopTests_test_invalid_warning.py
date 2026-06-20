# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeop.py
# case: CodeopTests_test_invalid_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        self.assertInvalid("'\\e' 1")
    self.assertEqual(len(w), 1)
    self.assertEqual(w[0].category, DeprecationWarning)
    self.assertRegex(str(w[0].message), 'invalid escape sequence')
    self.assertEqual(w[0].filename, '<input>')
