# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_error_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(s):
        with self.assertRaises(ValueError, msg='float(%r)' % (s,)) as cm:
            float(s)
        self.assertEqual(str(cm.exception), 'could not convert string to float: %r' % (s,))
    check('½')
    check('123½')
    check('  123 456  ')
    check(b'  123 456  ')
    check('')
    check(' ')
    check('\t \n')
    check('٣١٤!')
    check('123\x00')
    check('123\x00 245')
    check('123\x00245')
    check(b'123\x00')
    check(b'123\xa0')
