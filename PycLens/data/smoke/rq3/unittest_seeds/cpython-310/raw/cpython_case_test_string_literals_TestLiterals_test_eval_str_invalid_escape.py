# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string_literals.py
# case: TestLiterals_test_eval_str_invalid_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for b in range(1, 128):
        if b in b'\n\r"\'01234567NU\\abfnrtuvx':
            continue
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(eval("'\\%c'" % b), '\\' + chr(b))
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always', category=DeprecationWarning)
        eval("'''\n\\z'''")
    self.assertEqual(len(w), 1)
    self.assertEqual(w[0].filename, '<string>')
    self.assertEqual(w[0].lineno, 1)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('error', category=DeprecationWarning)
        with self.assertRaises(SyntaxError) as cm:
            eval("'''\n\\z'''")
        exc = cm.exception
    self.assertEqual(w, [])
    self.assertEqual(exc.filename, '<string>')
    self.assertEqual(exc.lineno, 1)
    self.assertEqual(exc.offset, 1)
