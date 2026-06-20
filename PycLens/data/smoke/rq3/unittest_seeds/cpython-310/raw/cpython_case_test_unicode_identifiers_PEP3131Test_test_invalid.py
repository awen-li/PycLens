# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode_identifiers.py
# case: PEP3131Test_test_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        from test import badsyntax_3131
    except SyntaxError as err:
        self.assertEqual(str(err), "invalid character '€' (U+20AC) (badsyntax_3131.py, line 2)")
        self.assertEqual(err.lineno, 2)
        self.assertEqual(err.offset, 1)
    else:
        self.fail("expected exception didn't occur")
