# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_base64errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertIncorrectPadding(data):
        with self.assertRaisesRegex(binascii.Error, '(?i)Incorrect padding'):
            binascii.a2b_base64(self.type2test(data))
    assertIncorrectPadding(b'ab')
    assertIncorrectPadding(b'ab=')
    assertIncorrectPadding(b'abc')
    assertIncorrectPadding(b'abcdef')
    assertIncorrectPadding(b'abcdef=')
    assertIncorrectPadding(b'abcdefg')
    assertIncorrectPadding(b'a=b=')
    assertIncorrectPadding(b'a\nb=')

    def assertInvalidLength(data):
        n_data_chars = len(re.sub(b'[^A-Za-z0-9/+]', b'', data))
        expected_errmsg_re = '(?i)Invalid.+number of data characters.+' + str(n_data_chars)
        with self.assertRaisesRegex(binascii.Error, expected_errmsg_re):
            binascii.a2b_base64(self.type2test(data))
    assertInvalidLength(b'a')
    assertInvalidLength(b'a=')
    assertInvalidLength(b'a==')
    assertInvalidLength(b'a===')
    assertInvalidLength(b'a' * 5)
    assertInvalidLength(b'a' * (4 * 87 + 1))
    assertInvalidLength(b'A\tB\nC ??DE')
