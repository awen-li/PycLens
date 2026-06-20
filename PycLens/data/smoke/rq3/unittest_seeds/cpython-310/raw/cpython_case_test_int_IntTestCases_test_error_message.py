# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_error_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(s, base=None):
        with self.assertRaises(ValueError, msg='int(%r, %r)' % (s, base)) as cm:
            if base is None:
                int(s)
            else:
                int(s, base)
        self.assertEqual(cm.exception.args[0], 'invalid literal for int() with base %d: %r' % (10 if base is None else base, s))
    check('½')
    check('123½')
    check('  123 456  ')
    check('123\x00')
    check('123\x00', 10)
    check('123\x00 245', 20)
    check('123\x00 245', 16)
    check('123\x00245', 20)
    check('123\x00245', 16)
    check(b'123\x00')
    check(b'123\x00', 10)
    check(b'123\xbd')
    check(b'123\xbd', 10)
    check('123\ud800')
    check('123\ud800', 10)
