# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_convert_stringval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = ((0, 0), ('09', 9), ('a', 'a'), ('áÚ', 'áÚ'), ([], '[]'), (None, 'None'))
    for (orig, expected) in tests:
        self.assertEqual(ttk._convert_stringval(orig), expected)
